#!/usr/bin/env python3
from boss_drp.utils import load_env
from boss_drp.utils.dailylogger import Formatter, emailLogger

import sys
    
try:
    from slurm import queue
    noslurm = False
    queue = queue()

except:
    import warnings
    class SlurmWarning(Warning):
        def __init__(self, message):
            self.message = message
    def __str__(self):
            return repr(self.message)
    warnings.warn('No slurm package installed: printing command to STDOUT for manual run',SlurmWarning)
    noslurm = True
    queue = None
    
import argparse
from os import getenv, makedirs
import os.path as ptt
from datetime import date
import astropy.time
from astropy.io import fits
from astropy.table import Table
import io
import pandas as pd
import logging
from pydl.pydlutils.yanny import yanny
import numpy as np
import time
import re



mjd = str(int(float(astropy.time.Time(str(date.today())).jd) - 2400000.5))

class Setup:
    def __init__(self):
        self.boss_spectro_redux = None
        self.run2d = None
        self.alloc = None
        self.nodes = 1
        self.ppn = None
        self.mem_per_cpu = None
        self.walltime = None
        self.shared = False
        self.fast = False
        self.epoch = False
        self.custom = None
        
    def __repr__(self):
        return self.__str__()
            
    def __str__(self):
        return (f"boss_spectro_redux: {self.boss_spectro_redux} \n"    +
                f"run2d: {self.run2d} \n"    +
                f"alloc: {self.alloc} \n"    +
                f"nodes: {self.nodes} \n"    +
                f"ppn: {self.ppn} \n"    +
                f"mem_per_cpu: {self.mem_per_cpu} \n"    +
                f"walltime: {self.walltime} \n"+
                f"fast: {self.fast} \n"+
                f"custom: {self.custom} \n"+
                f"epoch: {self.epoch} \n"+
                f"shared: {self.shared}");
        


def read_mod(fast=False, log=None, walltime='40:00:00', mem=128000, epoch=False,
             custom=None, full=False, boss_spectro_redux=None, run2d=None):
    setup = Setup()
    if boss_spectro_redux is None:
        setup.boss_spectro_redux = load_env('BOSS_SPECTRO_REDUX',log=log.info)
    else:
        setup.boss_spectro_redux = boss_spectro_redux
    if run2d is None:
        setup.run2d = load_env('RUN2D',log=log.info)
    else:
        setup.run2d = run2d
    if not noslurm:
        setup.alloc = load_env('SLURM_ALLOC', default='sdss-np')
    setup.nodes = 1 #load_env('SLURM_NODES')
    setup.ppn = 2
    setup.mem_per_cpu = mem
    setup.walltime = walltime
    setup.epoch=epoch
    setup.custom=custom

    if not noslurm:
        if setup.alloc.lower() == 'sdss-kp':
            kingspeak = True
            setup.shared = False
        else:
            kingspeak = False
            setup.shared = True
        if full:
            setup.share=False
            setup.ppn = load_env('SLURM_PPN', default=64)
            setup.mem_per_cpu = load_env('SLURM_MEM_PER_CPU', default=7500)
            fast = False
        if not kingspeak:
            if fast is True:
                setup.alloc = alloc+'-fast'
            
        setup.fast = fast

    return(setup)

def check_daily(mod, daily_dir, mjd, log):
    nextmjds = yanny(ptt.join(daily_dir, 'etc', 'nextmjd.par'))
    mods = np.char.lower(nextmjds["NEXTMJD"]['module'].astype(str))
    indx = np.where(mods == mod.lower())[0]
    if len(indx) == 0:
        return(False)
    else:
        return(nextmjds['NEXTMJD']['mjd'][indx].max() > mjd)

def check_fieldlist(boss_spectro_redux, run2d, spall_mjd):
    flist = Table(fits.getdata(ptt.join(boss_spectro_redux, run2d, 'fieldlist-'+run2d+'.fits'),1))
    r = re.compile('Done[\w]*', re.IGNORECASE)
    idx = [i for i, x in enumerate(flist['STATUS1D'].data ) if r.search(x)]
    flist = flist[idx]
    latest_redux = max(flist['MJD'])
    return(latest_redux > spall_mjd)

def slurm_fieldmerge(module='bhm/master', walltime = '40:00:00', fast = True, mem = 128000, daily=False,
                     epoch=False, custom=None, full=False):

    daily_dir = getenv('DAILY_DIR', default=None)
    if daily_dir is None: daily_dir = ptt.join(getenv('HOME'), "daily")

    makedirs(ptt.join(daily_dir, "logs", "fieldmerge", 'control'), exist_ok = True)
    filelog = logging.FileHandler(ptt.join(daily_dir, 'logs', 'fieldmerge', 'control', str(mjd)+'.log'))
    filelog.setLevel(logging.DEBUG)
    filelog.setFormatter(Formatter())

    logger = logging.getLogger()
    elog = emailLogger()
    emaillog = elog.log_handler
    emaillog.setLevel(logging.DEBUG)
    emaillog.setFormatter(Formatter())
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(Formatter())
    logger.addHandler(console)
    logger.addHandler(emaillog)
    logger.addHandler(filelog)
    logger.setLevel(logging.DEBUG)

    logger.info('===============================================')
    logger.debug(time.ctime())
    queue.verbose = True

    setup = read_mod(fast=fast, log=logger, walltime=walltime, mem=mem,
                     epoch=epoch, custom=custom)

    if daily is True: 
        with fits.open(ptt.join(setup.boss_spectro_redux, setup.run2d, 'spAll-'+run2d+'.fits')) as ff:
            tf = Table(ff[1].data)
            latest_mjd = tf['MJD'].max()
        
        if not check_daily(module, daily_dir, latest_mjd, logger):
            logger.debug('Skipping run')
            elog.send('fieldmerge '+setup.run2d +' MJD='+str(mjd), ptt.join(daily_dir, 'etc','emails'), logger)
            return()
        if not check_fieldlist(setup.boss_spectro_redux, setup.run2d, latest_mjd):
            logger.debug('SpAll-'+setup.run2d+' up to date')
            elog.send('fieldmerge '+setup.run2d +' MJD='+str(mjd), ptt.join(daily_dir, 'etc','emails'), logger)
            return()

    logger.info(setup)

    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    build(setup,daily_dir)
    
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    logger.info(output)
    
    if setup.epoch:
        subject = 'fieldmerge '+module +'epoch MJD='+str(mjd)
    elif setup.custom is not None:
        subject = 'fieldmerge '+module +f' {custom} MJD='+str(mjd)
    else:
        subject = 'fieldmerge '+module +' MJD='+str(mjd)
    elog.send(subject, ptt.join(daily_dir, 'etc','emails'), logger)
    logger.removeHandler(emaillog)
    emaillog.close()


def script(setup,daily_dir):
    cmddir = ptt.join(daily_dir, "cmd")
    if setup.epoch:
        cmd = f'run_fieldmerge_epoch_{setup.run2d}'
    elif setup.custom is not None:
        cmd = f'run_fieldmerge_{setup.custom}_{setup.run2d}'
    else:
        cmd = f'run_fieldmerge_{setup.run2d}'
        
    epochflag = ' --epoch' if setup.epoch else ''
    if not ptt.exist(ptt.join(cmddir, cmd)):
        makedirs(ptt.join(getenv('HOME'),'daily','cmd'),exist_ok=True)
        cmd = ['']
        cmd.append('#!/usr/bin/env bash')
        cmd.append('')
        cmd.append('cd $HOME/daily/logs')
        cmd.append('set -o verbose')
        cmd.append(f"fieldlist --create --run1d {run1d} --run2d {run2d} {epochflag}")
        cmd.append(f"fieldmerge --lite --include_bad --XCSAO {epochflag}")
        with open(ptt.join(cmddir, cmd),'w') as r:
            for c in cmd:
                r.write(c+'\n')
    
    return(cmddir,cmd)


def build(setup,daily_dir, title = None, obs=None):
    if title is None:
        title = 'fieldmerge_'+setup.run2d
        if epoch: title = title+'_epoch'
        if custom is not None:
            title = title+'_'+custom
    makedirs(logdir, exist_ok = True)

    log_folder = ptt.join(daily_dir, "logs", "fieldmerge", run2d)
    if epoch:
        log_folder = ptt.join(log_folder, 'epoch')
    if custom is not None:
        log_folder = ptt.join(log_folder, custom)
    log = ptt.join(log_folder, "fieldmerge_"+mjd)
    makedirs(log_folder, exist_ok = True)
    
    cmddir, cmd = script(setup,daily_dir)

    if obs is not None:
        lcoflag = ' --lco' if obs[0].upper() == 'LCO' else ''
    epochflag = ' --epoch' if epoch else ''

    if not noslurm:
        queue.create(label = title, nodes = setup.nodes, ppn = setup.ppn, walltime = setup.walltime,
                     alloc=setup.alloc, mem_per_cpu = setup.mem_per_cpu, shared = setup.shared)
        queue.append("source "+ptt.join(cmddir, cmd),
                     outfile = log+".o.log", errfile = log+".e.log")
        if obs is not None:
            queue.append(f"plot_QA    --run2d {setup.run2d} {lcoflag} {epochflag} ; ")
        queue.commit(submit=True)
    else:
        print("source "+ptt.join(cmddir, cmd))
        print(f"plot_QA    --run2d {setup.run2d} {lcoflag} {epochflag} ; ")
    return(queue)
    

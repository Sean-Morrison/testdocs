Full Command Documention
========================

BOSS_log

^^^^^^^^
 usage: BOSS_log [-h] [-m MJD] [-y] [-o {apo,lco}] [-l] [--new_ref] [-c] [-r]
                [-e] [-s]

Build BOSS Exposure Log

optional arguments:
  -h, --help            show this help message and exit
  -m MJD, --mjd MJD     MJD
  -y, --yesterday       current mjd-1
  -o {apo,lco}, --observatory {apo,lco}, --obs {apo,lco}
                        Manually set observatory
  -l, --long            Long/detailed version of log
  --new_ref             Calculate new reference values in fratio and w_shift
                        and show in place of fratio and w_shift (edit to code
                        to save new value is required)
  -c, --hide_hart, --hide_hartmann
                        Hide cleaned version of Hartmann Logs as a table
  -r, --hart_raw        Print raw form (instead of table form) of Hartmann
                        Logs
  -e, --hide_error      Hide SOS Error and Workings
  -s, --hide_summary    Hide data summary table
SOS

^^^
 usage: SOS [-h] (-r | -b | -j) (-c | -t | -d) [-e EXP] [-m [MJD [MJD ...]]]
           [--nodb] [--no_gz] [--no_reject] [--clobber_fibermap]
           [--no_sdssv_sn2] [-n] [-o] [-v]

SOS process for reducing BOSS data on the Moutain

optional arguments:
  -h, --help            show this help message and exit
  -r, --red             Red Camera Process
  -b, --blue            Blue Camera Process
  -j, --joint           Both Camera Processes
  -c, --catchup         Run Catchup on the night or (MJD)
  -t, --redoMode        Save outputs of MJD or exposure to sosredo
  -d, --test            Save outputs and logs to sosredo/dev
  -e EXP, --exp EXP     exposure id (or range of exp id 500-510) (with or
                        without leading zeros)
  -m [MJD [MJD ...]], --mjd [MJD [MJD ...]]
                        MJD
  --nodb                skip opsdb load
  --no_gz               Overrides the requirement for '.gz' compressed files
                        (experimental)
  --no_reject           Overrides the Calibration rejection (use with caution)
  --clobber_fibermap, -f
                        Clobbers the existing spfibermap files
  --no_sdssv_sn2        Skip reporting a second set of SN2 values with updated
                        fit parameters
  -n, --no_arc2trace    Skip Utilizing arc2trace refinements
  -o, --forcea2t        Force arc2trace for all fields (even if flat exists
                        for field)
  -v, --verbose         prints the only (or red if joint) active SOS process
                        to terminal
boss_arcs_to_traces

^^^^^^^^^^^^^^^^^^^
 Traceback (most recent call last):
  File "/uufs/chpc.utah.edu/common/home/u6037107/idlspec2d/cleanup/python/boss_drp/../../bin/boss_arcs_to_traces", line 7, in <module>
    from pyvista import boss
ModuleNotFoundError: No module named 'pyvista'
build_combined_html

^^^^^^^^^^^^^^^^^^^
 usage: build_combined_html [-h] [--force] sosdir

build SOS combine index page

positional arguments:
  sosdir      Base SOS output directory

optional arguments:
  -h, --help  show this help message and exit
  --force     Force update
cronrun.bash

^^^^^^^^^^^^
 usage: cronrun.bash module 'script'
 
fieldlist

^^^^^^^^^
 usage: fieldlist [-h] [--create] [--topdir TOPDIR]
                 [--run1d [RUN1D [RUN1D ...]]] [--run2d [RUN2D [RUN2D ...]]]
                 [--outdir OUTDIR] [--skipcart [SKIPCART [SKIPCART ...]]]
                 [--epoch] [--basehtml BASEHTML] [--logfile LOGFILE] [--debug]
                 [--noplot]

Build/load BOSS Fieldlist

optional arguments:
  -h, --help            show this help message and exit
  --create, -c          Create Fieldlist
  --topdir TOPDIR       Optional override value for the environment variable
                        $BOSS_SPECTRO_REDUX
  --run1d [RUN1D [RUN1D ...]]
                        Optional override value for the enviro variable $RUN1D
  --run2d [RUN2D [RUN2D ...]]
                        Optional override value for the enviro variable $RUN2D
  --outdir OUTDIR       Optional output directory (defaults to topdir/$RUN2D)
  --skipcart [SKIPCART [SKIPCART ...]]
                        Option list of cartridges to skip
  --epoch               Produce FieldList for epoch coadds
  --basehtml BASEHTML   html path for figure (defaults to relative from
                        topdir)
  --logfile LOGFILE     Manually Set logfile (including path)
  --debug               Overrides the logger of the simplified error messages
                        and prints standard python errors
  --noplot              Skips updating the sky plots
fieldmerge

^^^^^^^^^^
 usage: fieldmerge [-h] [--run2d RUN2D] [--indir INDIR] [--skip_line]
                  [--include_bad] [--legacy] [--skip_specprimary] [--lite]
                  [--XCSAO] [--field FIELD] [--mjd MJD] [--clobber]
                  [--verbose] [--logfile LOGFILE] [--epoch]
                  [--programs [PROGRAMS [PROGRAMS ...]]]
                  [--datamodel DATAMODEL] [--line_datamodel LINE_DATAMODEL]
                  [--outroot OUTROOT] [--remerge_fmjd REMERGE_FMJD]
                  [--merge_only] [--allsky] [--custom CUSTOM] [--run1d RUN1D]
                  [--limit LIMIT] [--ndays MJDSTART]

Build BOSS spAll Summary File

optional arguments:
  -h, --help            show this help message and exit
  --run2d RUN2D         Optional override value for the enviro variable $RUN2D
  --indir INDIR         Optional override value for the environment variable
                        $BOSS_SPECTRO_REDUX
  --skip_line           skip the generation of spAllLine.fits
  --include_bad         include bad fields
  --legacy              Include columns used by SDSS-IV and depreciated in
                        SDSS-V
  --skip_specprimary    Skip creation of specprimary and associated columns
  --lite                Produce lite version of spAll file
  --XCSAO               Include XCSAO columns
  --field FIELD, -f FIELD
                        Run for a single Field
  --mjd MJD, -m MJD     Run for a single MJD
  --clobber             Clobber all spAll-field-mjd files
  --verbose             Log columns not saved
  --logfile LOGFILE     Manually set logfile
  --epoch               Produce spAll for epoch coadds
  --programs [PROGRAMS [PROGRAMS ...]]
                        List of programs to include
  --datamodel DATAMODEL
                        Supply a spAll datamodel file (defaults to
                        $IDLSPEC2D/datamodel/spall_dm.par)
  --line_datamodel LINE_DATAMODEL
                        Supply a spline datamodel file (defaults to
                        $IDLSPEC2D/datamodel/spzline_dm.par)
  --outroot OUTROOT     Path and root of filename for output (defaults to
                        $BOSS_SPECTRO_REDUX/$RUN2D/{field}/{mjd}/spAll)
  --remerge_fmjd REMERGE_FMJD, -r REMERGE_FMJD
                        Field-MJD to replace in spAll
  --merge_only, -o      Skip Building new spAll-Field-MJD files and just merge
                        existing
  --allsky              Build spAll for Allsky Custom Coadd
  --custom CUSTOM       Name of Custom Coadd
  --run1d RUN1D         Optional override value for the enviro variable $RUN1D
                        (only for custom allsky coadds)
  --limit LIMIT         Limit number of Field-MJD spAll files to read before
                        save
  --ndays MJDSTART      Limit update to last ndays
filecheck

^^^^^^^^^
 usage: filecheck [-h] cmd file

        Check File (uncompressed or gz) favor/instrument/quality
        
        science:
          return "true" if the fits file is a science frame.  This
          is determined by flavor=science in the header.  If flavor
          is not in the header, "false" is returned.
    
        test:
          return "true" if the fits file is a test frame.  This is
          determined by quality=test in the header.  If quality
          is not in the header, "false" is returned
    
        excellent:
          return "true" if the fits file is a excellent frame.  This is
          determined by quality=excellent in the header.  If quality
          is not in the header, "true" is returned
    
        boss:
          return "true" if the plPlugMapM file is a boss frame.
          this is determined by instrument=boss in the header.
          If instrument is not in the header, "false" is returned.
        

positional arguments:
  cmd         file check command
  file        fits file

optional arguments:
  -h, --help  show this help message and exit
fluxcorr_prior

^^^^^^^^^^^^^^
 usage: fluxcorr_prior [-h] [--xythrucorr] planfile

Try solving with a prior that fluxcorr = 1

positional arguments:
  planfile

optional arguments:
  -h, --help    show this help message and exit
  --xythrucorr
idlspec2d_version

^^^^^^^^^^^^^^^^^
 usage: idlspec2d_version
 
loadSN2Value

^^^^^^^^^^^^
 usage: loadSN2Value [-h] [-v] [-u] [--sdssv_sn2] fits confSum

Load SOS SN2 values into OpsDB

positional arguments:
  fits           The fits file is the science frame output from sos-reduce
  confSum        confSummary-file

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  verbose
  -u, --update   update (An error will occur if the exposure has already been
                 processed, unless set)
  --sdssv_sn2    sdssv_sn2
manage_coadd_Schema

^^^^^^^^^^^^^^^^^^^
 usage: manage_coadd_Schema [-h] [--coaddfile COADDFILE] [--topdir TOPDIR]
                           [--run2d RUN2D] [--name NAME] [--DR] [--rerun1d]
                           [--active] [--carton [CARTON [CARTON ...]]]
                           [--SDSSIDS [SDSSIDS [SDSSIDS ...]]]
                           [--program [PROGRAM [PROGRAM ...]]]
                           [--legacy [LEGACY [LEGACY ...]]] [--use_catid]
                           [--use_firstcarton] [--cadence CADENCE] [--show]
                           [--mjd [MJD [MJD ...]]]

Manage Custom Coadds

optional arguments:
  -h, --help            show this help message and exit
  --coaddfile COADDFILE, -f COADDFILE
                        File to store Coadding Schema (Default:
                        {topdir}/{run2d}/SDSSV_BHM_COADDS.par
  --topdir TOPDIR       Override value for the environment variable
                        $BOSS_SPECTRO_REDUX.
  --run2d RUN2D         Override value for the environment variable $RUN2D
  --name NAME           Name of Custom Coadd
  --DR                  DR/IPL Coadding
  --rerun1d, -r         Provides flag for coadd to be rerun though 1D analysis
  --active, -a          Activate (or deactivate) a Coadding Schema
  --carton [CARTON [CARTON ...]], -c [CARTON [CARTON ...]]
                        list of cartons
  --SDSSIDS [SDSSIDS [SDSSIDS ...]], -i [SDSSIDS [SDSSIDS ...]]
                        list of SDSS_IDS (or CatalogIDs if use_catid is set)
  --program [PROGRAM [PROGRAM ...]], -p [PROGRAM [PROGRAM ...]]
                        list of programs
  --legacy [LEGACY [LEGACY ...]], -l [LEGACY [LEGACY ...]]
                        list of Legacy Tags to include
  --use_catid, -u       Use CatalogIDs rather then SDSS_IDs
  --use_firstcarton     Use Firstcarton only for carton match (dont look at
                        db)
  --cadence CADENCE, -t CADENCE
                        Number of days between coadd epochs
  --show, -s            Show Configurations
  --mjd [MJD [MJD ...]]
                        Use data from these MJDs.
read_sos

^^^^^^^^
 usage: read_sos [-h] [--exp EXP] [--nocopy] directory mjd

Create Fiber info Summary for SOS

positional arguments:
  directory          SOS Directory
  mjd                mjd

optional arguments:
  -h, --help         show this help message and exit
  --exp EXP, -e EXP  Exposure Name
  --nocopy, -n       Prevent copy to combined Directory
readfibermaps

^^^^^^^^^^^^^
 usage: readfibermaps [-h] [-p SPPLAN2D] [--topdir TOPDIR] [-c] [--fast]
                     [--datamodel DATAMODEL] [-s] [--release RELEASE]
                     [--remote] [--dr19] [--confSummary CONFSUMMARY]
                     [--ccd {b2,r2,b1,r1}] [--mjd MJD] [--log]

Produces spfibermap file corresponding to a spplan2d (or single confSummary
file for SOS)

optional arguments:
  -h, --help            show this help message and exit
  -p SPPLAN2D, --spplan2d SPPLAN2D
                        spplan2d file for idlspec2d run
  --topdir TOPDIR       Alternative output directory (defaults to location of
                        spplan2d file or /data/boss/sos/{mjd} for SOS)
  -c, --clobber         overwrites previous spfibermap file
  --fast                When using --no_db, streamlines process and only gets
                        parallax from MOS target files
  --datamodel DATAMODEL
                        Supply a datamodel file (defaults to
                        $IDLSPEC2D/datamodel/spfibermap_dm.par or
                        $IDLSPEC2D/datamodel/spfibermap_sos_dm.par for SOS)
  -s, --SOS             produces spfibermap for SOS
  --release RELEASE     sdss_access data release (defaults to sdsswork),
                        required if you do not have proprietary access,
                        otherwise see https://sdss-
                        access.readthedocs.io/en/latest/auth.html#auth
  --remote              allow for remote access to data using sdss-access
  --dr19                Limit targeting flags to DR19 cartons

SOS:
  Options of use with SOS only

  --confSummary CONFSUMMARY
                        confSummary file for SOS (required for with --SOS)
  --ccd {b2,r2,b1,r1}   CCD for SOS
  --mjd MJD             MJD of observation
  --log                 creates log file in topdir
run_PyXCSAO

^^^^^^^^^^^
 usage: run_PyXCSAO [-h] [--run1d RUN1D] [--epoch] fitsfile

Runs pyXCSAO to determine RVs

positional arguments:
  fitsfile              fits file

optional arguments:
  -h, --help            show this help message and exit
  --run1d RUN1D, -r RUN1D
                        run1d name
  --epoch               run for epoch Coadds
sdR_hdrfix

^^^^^^^^^^
 usage: sdR_hdrfix [-h] [--mjd MJD] [--obs {APO,LCO}] [--clobber]
                  [--cameras {b1,b2,r1,r2,??}] [--bad] [--test]
                  [--FF {0,1} {0,1} {0,1} {0,1}]
                  [--FFS {0,1} {0,1} {0,1} {0,1} {0,1} {0,1} {0,1} {0,1}]
                  [--NE {0,1} {0,1} {0,1} {0,1}]
                  [--HGCD {0,1} {0,1} {0,1} {0,1}]
                  [--HEAR {0,1} {0,1} {0,1} {0,1}] [--arc] [--flat]
                  [--hartmann {Out,Right,Left,Closed}]
                  [--quality {excellent,test,bad}]
                  [--flavor {bias,dark,flat,arc,science,smear}]
                  [--exptime EXPTIME] [--tai-beg TAI_BEG]
                  [--cartid {FPS-S,FPS-N}] [--fieldid FIELDID]
                  [--confid CONFIGID] [--designid DESIGNID] [--key KEY]
                  [--value VALUE]
                  expid

Create the files used by the pipeline to fix the header meta data of the BOSS
exposures

positional arguments:
  expid                                                  Exposure ID

optional arguments:
  -h, --help                                             show this help
                                                         message and exit
  --mjd MJD, -m MJD                                      mjd of file (default:
                                                         latest MJD)
  --obs {APO,LCO}                                        Set Observatory
                                                         (default:APO)
  --clobber                                              clobber sdHdrFix file
  --cameras {b1,b2,r1,r2,??}                             Cameras for hdr
                                                         update (?? for all
                                                         cameras) [default:??]

Optional Quality Update (exclusive)
    [31mAt current only use if still exposing or don't run SOS after (skip and note in Night Log (and/or email) if uncertain)[0m:
  --bad, -b                                              flag as quality=bad
  --test, -t                                             flag as quality=test

Optional lamp/screen keys to Update (1:on, 0:off):
  --FF {0,1} {0,1} {0,1} {0,1}                           Flat Field Lamp
  --FFS {0,1} {0,1} {0,1} {0,1} {0,1} {0,1} {0,1} {0,1}  Flat Field Screen
  --NE {0,1} {0,1} {0,1} {0,1}                           Ne arc lamp
  --HGCD {0,1} {0,1} {0,1} {0,1}                         HeCd arc Lamp
  --HEAR {0,1} {0,1} {0,1} {0,1}                         HeAr arc Lamp
  --arc                                                  short cut to set all
                                                         relevant arc lamps to
                                                         1 1 1 1
  --flat                                                 short cut to set FF =
                                                         1 1 1 1 & FFS = 1 1 1
                                                         1 1 1 1 1
  --hartmann {Out,Right,Left,Closed}                     Hartmann Door Status

Optional Common keys to Update
    [31mAt current only use if still exposing or don't run SOS after (skip and note in Night Log (and/or email) if uncertain)[0m:
  --quality {excellent,test,bad}                         Set Quality flat of
                                                         exposures

Optional Specialized Keys to Update 
    [31m Only use if still exposing or don't run SOS after (skip and note in Night Log (and/or email) if uncertain)[0m:
  --flavor {bias,dark,flat,arc,science,smear}            Type/Flavor of
                                                         exposure
  --exptime EXPTIME                                      Exposure length (s)
  --tai-beg TAI_BEG                                      Starting time (tai)
                                                         of exposure
  --cartid {FPS-S,FPS-N}                                 Cartridge Mounted
  --fieldid FIELDID                                      FieldID
  --confid CONFIGID                                      ConfigureID
  --designid DESIGNID                                    DesignID

Manually update a key 
    [31m Only use if still exposing or don't run SOS after (skip and note in Night Log (and/or email) if uncertain)[0m:
  --key KEY, -k KEY                                      header keyword to
                                                         update (required if
                                                         value is set)
  --value VALUE, -v VALUE                                updated header
                                                         keyword value
                                                         (required if key is
                                                         set)

one or more update options are required
slurm_fieldmerge

^^^^^^^^^^^^^^^^
 usage: slurm_fieldmerge [-h] [--module MODULE] [--walltime WALLTIME] [--fast]
                        [--mem MEM] [--daily]

Create daily field merge slurm job. Without access to the SDSS Slurm package,
it prints the commands for manual execution

optional arguments:
  -h, --help            show this help message and exit
  --module MODULE, -m MODULE
                        module file to use (ex bhm/master[default] or
                        bhm/v6_0_9)
  --walltime WALLTIME, -w WALLTIME
                        Job wall time (format hh:mm:ss) default = "40:00:00"
  --fast                use fast allocation
  --mem MEM             memory in bytes
  --daily               only run if daily run has been run today
slurm_readfibermap

^^^^^^^^^^^^^^^^^^
 usage: slurm_readfibermap [-h] [--module MODULE] [--topdir TOPDIR]
                          [--run2d RUN2D] [--clobber] [--apo] [--lco] [--dr19]
                          [--mjd [MJD [MJD ...]]] [--mjdstart MJDSTART]
                          [--mjdend MJDEND] [--mem_per_cpu MEM_PER_CPU]
                          [--walltime WALLTIME] [--ppn PPN]

Create daily field merge slurm job. Without access to the SDSS Slurm package,
it prints the commands for manual execution

optional arguments:
  -h, --help            show this help message and exit
  --module MODULE, -m MODULE
                        module file to use (ex bhm/master or bhm/v6_0_9)
  --topdir TOPDIR       Boss Spectro Redux base directory
  --run2d RUN2D         Run2d
  --clobber             Clobber spfibermaps
  --apo                 run apo
  --lco                 run lco
  --dr19                Limit targeting flags to DR19 cartons

Select MJDs:
  --mjd [MJD [MJD ...]]
                        MJD dates to reduce; default="*"
  --mjdstart MJDSTART   Starting MJD
  --mjdend MJDEND       Ending MJD

Slurm Options:
  --mem_per_cpu MEM_PER_CPU
                        Memory allocated per CPU
  --walltime WALLTIME   Wall time in hours
  --ppn PPN             Number of processors per node
slurm_sos

^^^^^^^^^
 usage: slurm_sos [-h] [--apo] [--lco] [--mjd [MJD [MJD ...]]]
                 [--mjdstart MJDSTART] [--mjdend MJDEND] [--no_reject]
                 [--clobber_fibermap] [--no_sdssv_sn2] [-n] [-o] [--a2t]
                 [--mem_per_cpu MEM_PER_CPU] [--walltime WALLTIME]
                 [--nodes NODES] [--ppn PPN] [--no_submit]

Create SOS slurm job. Without access to the SDSS Slurm package, it prints the
commands for manual execution

optional arguments:
  -h, --help            show this help message and exit
  --apo                 run apo
  --lco                 run lco

Select MJDs:
  --mjd [MJD [MJD ...]]
                        MJD dates to reduce; default=Today
  --mjdstart MJDSTART   Starting MJD
  --mjdend MJDEND       Ending MJD

SOS Options:
  --no_reject           Overrides the Calibration rejection (use with caution)
  --clobber_fibermap, -f
                        Clobbers the existing spfibermap files
  --no_sdssv_sn2        Skip reporting a second set of SN2 values with updated
                        fit parameters
  -n, --no_arc2trace    Skip Utilizing arc2trace refinements
  -o, --forcea2t        Force arc2trace for all fields (even if flat exists
                        for field)
  --a2t

Slurm Options:
  --mem_per_cpu MEM_PER_CPU
                        Memory allocated per CPU
  --walltime WALLTIME   Wall time in hours
  --nodes NODES         Number of nodes to use; default=1
  --ppn PPN             Number of processors per node
  --no_submit           Skip submitting process to queue
slurm_spTrace

^^^^^^^^^^^^^
 usage: slurm_spTrace [-h] [--module MODULE] [--topdir TOPDIR] [--run2d RUN2D]
                     [--mjd [MJD [MJD ...]]] [--mjdstart MJDSTART]
                     [--mjdend MJDEND] [--lco] [--clobber] [--debug]
                     [--skip_plan]

Create spTrace slurm jobs. Without access to the SDSS Slurm package, it prints
the commands for manual execution.

optional arguments:
  -h, --help            show this help message and exit
  --module MODULE, -m MODULE
                        module file to use (ex bhm/master or bhm/v6_0_9)
  --topdir TOPDIR       Boss Spectro Redux base directory
  --run2d RUN2D         Run2d
  --mjd [MJD [MJD ...]]
  --mjdstart MJDSTART
  --mjdend MJDEND
  --lco
  --clobber
  --debug
  --skip_plan
sos_command

^^^^^^^^^^^
 usage: sos_command -f name -i path -p name -l path -s path -m 00000 [-d -e]
 
   -f    Fits file name
   -i    Fits file directory path
   -p    Plugmap file name
   -l    Plugmap file directory path
   -s    SOS Directory
   -m    MJD
 
   -d    Dry run.
   -e    FPS mode
   -a    no cal mode
   -n    no OpsDB upload
   -v    calculate SN2_v2 (SDSS-V)
 
All parameters except -d, -a, and -e are required, FPS mode is set by default.
Normally sos_command will be called by sos_runnerd.
spSpec_reformat

^^^^^^^^^^^^^^^
 usage: spSpec_reformat [-h] --field FIELD --mjd MJD [--topdir TOPDIR]
                       [--run2d RUN2D] [--run1d RUN1D] [--custom CUSTOM]
                       [--plot] [--epoch] [--lsdr10] [--allsky]

Build Spec Files

optional arguments:
  -h, --help            show this help message and exit
  --field FIELD, -f FIELD
                        Run for a single Field
  --mjd MJD, -m MJD     Run for a single MJD
  --topdir TOPDIR       Optional override value for the environment variable
                        $BOSS_SPECTRO_REDUX
  --run2d RUN2D         Optional override value for the enviro variable $RUN2D
  --run1d RUN1D         Optional override value for the enviro variable $RUN2D
  --custom CUSTOM       Name of Custom Coadd schema
  --plot, -p            Create spec plots
  --epoch, -e           Run for epoch Coadds
  --lsdr10              Include Legacy Survey DR10 links on HTML
  --allsky              Include Legacy Survey DR10 links on HTML
spplan

^^^^^^
 usage: spplan [-h] [--skip2d] [--skip1d] [--module MODULE] [--topdir TOPDIR]
              [--run2d RUN2D] [--lco] [--logfile LOGFILE] [--verbose VERBOSE]
              [-c] [--release RELEASE] [--remote] [--override_manual]
              [--mjd [MJD [MJD ...]]] [--mjdstart MJDSTART] [--mjdend MJDEND]
              [--field [FIELD [FIELD ...]]] [--fieldstart FIELDSTART]
              [--fieldend FIELDEND] [--legacy] [--plates] [--fps] [--sdssv]
              [--no_commissioning] [--no_dither] [--matched_flats]
              [--nomatched_arcs] [--minexp MINEXP] [--single_flat]
              [--multiple_arc] [--manual_noarc] [--plate_epoch] [--quick]

Produce the spPlan2d and spPlancomb files for the pipeline run

optional arguments:
  -h, --help            show this help message and exit

General:
  General Setup Options

  --skip2d              Skip spplan2d
  --skip1d              Skip spplan1d
  --module MODULE       Module file to load for run
  --topdir TOPDIR       Base run2d directory to override module or
                        environmental variable
  --run2d RUN2D         Run2d to override module or environmental variable
  --lco                 Build Run files for LCO
  --logfile LOGFILE     Optional logfile (Including path)
  --verbose VERBOSE     Provide information about nonutlized frames
  -c, --clobber         overwrites previous plan file
  --release RELEASE     sdss_access data release (defaults to sdsswork),
                        required if you do not have proprietary access,
                        otherwise see https://sdss-
                        access.readthedocs.io/en/latest/auth.html#auth
  --remote              allow for remote access to data using sdss-access
  --override_manual     Override/clobber manually edited plan

MJD/Field Filtering:
  MJD/Field Filtering Options

  --mjd [MJD [MJD ...]]
                        Use data from these MJDs.
  --mjdstart MJDSTART   Starting MJD
  --mjdend MJDEND       Ending MJD
  --field [FIELD [FIELD ...]]
                        Use data from these fields.
  --fieldstart FIELDSTART
                        Starting Field
  --fieldend FIELDEND   Ending Field
  --legacy              Include legacy (BOSS/eBOSS) plates
  --plates              Include SDSS-V plates
  --fps                 Include FPS Fields
  --sdssv               Include both SDSS-V Fields & Plates
  --no_commissioning    Exclude SDSS-V FPS Commission Fields
  --no_dither           Exclude Dither fields

RUN2D:
  spPlan2d Setup Options

  --matched_flats       Require Flat from a field/plate
  --nomatched_arcs      Allow Arc from another field/plate
  --minexp MINEXP       Min Science Exposures in Plan (default=1)
  --single_flat         Only find the closest flat calibration frame
  --multiple_arc        Find all possible arc calibration frames
  --manual_noarc        if nomatched_arcs is False, builds spplan with
                        unmatched arcs and mark as manual

RUN1D:
  spPlancomb Setup Options

  --plate_epoch         Use a variable max epoch length for plate coadd
  --quick               Use the list of new spPlan2d as a filter for fields
spplan_epoch

^^^^^^^^^^^^
 usage: spplan_epoch [-h] [--module MODULE] [--topdir TOPDIR] [--run2d RUN2D]
                    [--run1d RUN1D] [--mjd MJD] [--mjdstart MJDSTART]
                    [--mjdend MJDEND] [--fieldid FIELDID]
                    [--fieldst FIELDSTART] [--fieldend FIELDEND] [--fps]
                    [--sdssv] [--clobber] [--minexp MINEXP] [--lco]
                    [--logfile LOGFILE] [--abandoned] [--started]
                    [--min_epoch_len MIN_EPOCH_LEN] [--release RELEASE]
                    [--remote]

Builds the spPlancombepoch files

optional arguments:
  -h, --help            show this help message and exit
  --module MODULE       Module file to load for run
  --topdir TOPDIR       Override value for the environment variable
                        $BOSS_SPECTRO_REDUX.
  --run2d RUN2D         Override value for the environment variable $RUN2D
  --run1d RUN1D         Override value for the environment variable $RUN1D
  --mjd MJD             Use data from these MJDs.
  --mjdstart MJDSTART   Starting MJD
  --mjdend MJDEND       Ending MJD
  --fieldid FIELDID     Look for the input data files in topdir/fieldid;
                        default to search all subdirectories. Note that this
                        need not be integer-valued, but could be for example
                        '0306_test'.
  --fieldst FIELDSTART  Starting fieldid
  --fieldend FIELDEND   Ending fieldid
  --fps                 Only produce epoch coadds for FPS Fields
                        (Fields>16000)
  --sdssv               Only produce epoch coadds for SDSS-V Fields
                        (Fields>15000)
  --clobber             If set, then over-write conflicting plan files
  --minexp MINEXP       Set minimum number of Science Frames for plan creation
  --lco                 Create Plans for LCO
  --logfile LOGFILE, -l LOGFILE
                        File for logging
  --abandoned           Create plans for abandoned epochs
  --started             Create plans for started epochs (including unfinished)
  --min_epoch_len MIN_EPOCH_LEN
                        minimum length of epoch required to produce plan
  --release RELEASE     sdss_access data release (defaults to sdsswork),
                        required if you do not have proprietary access,
                        otherwise see https://sdss-
                        access.readthedocs.io/en/latest/auth.html#auth
  --remote              allow for remote access to data using sdss-access
spplan_target

^^^^^^^^^^^^^
 usage: spplan_target [-h] (--manual | --batch) [--module MODULE] [--name NAME]
                     [--coaddfile COADDFILE] [--topdir TOPDIR] [--run2d RUN2D]
                     [--run1d RUN1D] [--clobber] [--logfile LOGFILE] [--DR]
                     [--cartons [CARTONS [CARTONS ...]]]
                     [--catalogids [CATALOGIDS [CATALOGIDS ...]]]
                     [--program [PROGRAM [PROGRAM ...]]]
                     [--mjd [MJD [MJD ...]]] [--mjdstart MJDSTART]
                     [--mjdend MJDEND] [--coadd_mjdstart COADD_MJDSTART]
                     [--rerun1d] [--use_catid] [--use_firstcarton] [--useDB]
                     [--lco]

Build CatalogID Combine Plan

optional arguments:
  -h, --help            show this help message and exit
  --manual              Manaully run a Coadd Schema (from coaddfile if only
                        name is set)
  --batch               Batch run all active Coadd Schema in batch file
                        located {topdir}/{run2d}/{name}
  --module MODULE       Module file to load for run
  --name NAME           Name of Custom Coadd
  --coaddfile COADDFILE
                        File of store Coadding Schema
  --topdir TOPDIR       Override value for the environment variable
                        $BOSS_SPECTRO_REDUX.
  --run2d RUN2D         Override value for the environment variable $RUN2D
  --run1d RUN1D         Override value for the environment variable $RUN1D
  --clobber             If set, then over-write conflicting plan files
  --logfile LOGFILE     File for logging
  --DR                  DR/IPL Batch Coadding
  --cartons [CARTONS [CARTONS ...]]
                        list of cartons
  --catalogids [CATALOGIDS [CATALOGIDS ...]]
                        list of sdss_ids (or catalogids)
  --program [PROGRAM [PROGRAM ...]]
                        list of programs
  --mjd [MJD [MJD ...]]
                        Use data from these MJDs.
  --mjdstart MJDSTART   Starting MJD
  --mjdend MJDEND       Ending MJD
  --coadd_mjdstart COADD_MJDSTART
                        First Coadd MJD to include
  --rerun1d             Provides flag for coadd to be rerun though 1D analysis
  --use_catid, -u       Uses CatalogID rather then sdss_id
  --use_firstcarton     Use Firstcarton only for carton match (dont look at
                        db)
  --useDB               Use sdss targetdb instead of the Semaphore targeting
                        flag (if not use_firstcarton)
  --lco                 Create Plans for LCO
spplan_trace

^^^^^^^^^^^^
 usage: spplan_trace [-h] [--module MODULE] [--topdir TOPDIR] [--run2d RUN2D]
                    [--lco] [--logfile LOGFILE] [--verbose VERBOSE] [-c]
                    [--release RELEASE] [--remote] [--override_manual]
                    [--mjd [MJD [MJD ...]]] [--mjdstart MJDSTART]
                    [--mjdend MJDEND] [--legacy] [--plates] [--fps] [--sdssv]

Produces spPlanTrace

optional arguments:
  -h, --help            show this help message and exit

General:
  General Setup Options

  --module MODULE       Module file to load for run
  --topdir TOPDIR
  --run2d RUN2D         Run2d to override module or environmental variable
  --lco                 Build Run files for LCO
  --logfile LOGFILE     Optional logfile (Including path)
  --verbose VERBOSE     Provide information about nonutlized frames
  -c, --clobber         overwrites previous plan file
  --release RELEASE     sdss_access data release (defaults to sdsswork),
                        required if you do not have proprietary access,
                        otherwise see https://sdss-
                        access.readthedocs.io/en/latest/auth.html#auth
  --remote              allow for remote access to data using sdss-access
  --override_manual     Override/clobber manually edited plan

MJD/Field Filtering:
  MJD/Field Filtering Options

  --mjd [MJD [MJD ...]]
                        Use data from these MJDs.
  --mjdstart MJDSTART   Starting MJD
  --mjdend MJDEND       Ending MJD
  --legacy              Include legacy (BOSS/eBOSS) plates
  --plates              Include SDSS-V plates
  --fps                 Include FPS Fields
  --sdssv               Include both SDSS-V Fields & Plates
sxpar.py

^^^^^^^^
 usage: sxpar.py [-h] [-v] fitsfile keyword

Simply parse a fits header

positional arguments:
  fitsfile       The fits file to read
  keyword        Header keyword to parse

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  verbose
sxpar_retry.py

^^^^^^^^^^^^^^
 usage: sxpar_retry.py [-h] [-v] fitsfile keyword

Simply parse a fits header, retrying if failed

positional arguments:
  fitsfile       The fits file to read
  keyword        Header keyword to parse

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  verbose
update_flags

^^^^^^^^^^^^
 usage: update_flags [-h] [--run2d RUN2D] [--topdir TOPDIR] [--clobber]
                    [--custom [CUSTOM [CUSTOM ...]]] [--nobackup]

Update SDSSV Targeting flats inn the summary files

optional arguments:
  -h, --help            show this help message and exit
  --run2d RUN2D         idlspec2d Run2d version
  --topdir TOPDIR       idlspec2d Run2d topdir
  --clobber             Clobber spTargeting file
  --custom [CUSTOM [CUSTOM ...]]
                        List of name of custom coadd schema
  --nobackup            Skip backup of existing
uubatchpbs

^^^^^^^^^^
 usage: uubatchpbs [-h] [--sdssv] [--sdssv_fast] [--sdssv_noshare] [--apo]
                  [--lco] [--bay15] [--merge3d] [--obs [OBS [OBS ...]]]
                  [--topdir TOPDIR] [--run1d RUN1D] [--run2d RUN2D]
                  [--idlutils_1d IDLUTILS_1D] [--no_reject] [--MWM_fluxer]
                  [--map3d {bayestar15,bay15,merge3d}] [--no_healpix]
                  [--noxcsao] [--skip_specprimary] [--no_merge_spall]
                  [--skip2d] [--only1d] [--onestep_coadd] [--fibermap_clobber]
                  [--saveraw] [--debug] [--no_db] [--fast_no_db FAST_NO_DB]
                  [--sdss_access_release SDSS_ACCESS_RELEASE]
                  [--sdss_access_remote] [--dr19] [--a2t]
                  [--fieldids [FIELDIDS [FIELDIDS ...]]]
                  [--fieldstart FIELDSTART] [--fieldend FIELDEND]
                  [--mjd [MJD [MJD ...]]] [--mjdstart MJDSTART]
                  [--mjdend MJDEND] [--no_write] [--shared] [--fast]
                  [--mem_per_cpu MEM_PER_CPU] [--walltime WALLTIME]
                  [--nodes NODES] [--ppn PPN] [--nosubmit] [--clobber]
                  [--epoch] [--custom CUSTOM] [--allsky] [--coadd_only]
                  [--1dpost] [--email]

Build idlspec2d redux and submit to slurm. Without access to the SDSS Slurm
package, it prints the commands for manual execution

optional arguments:
  -h, --help            show this help message and exit

Short cuts:
  --sdssv               --mwm, --no_merge_spall, --no_reject
  --sdssv_fast
  --sdssv_noshare
  --apo
  --lco
  --bay15               Set map3d to bayestar15 model
  --merge3d             Set map3d to best 3d model

idlspec2d Run options:
  --obs [OBS [OBS ...]]
                        Observatory {apo,lco}
  --topdir TOPDIR       Optional override value for the environment variable
                        $BOSS_SPECTRO_REDUX
  --run1d RUN1D         Optional override value for the enviro variable $RUN1D
  --run2d RUN2D         Optional override value for the enviro variable $RUN2D
  --idlutils_1d IDLUTILS_1D
                        idlutils override version of spec1d
  --no_reject           Deactivate Rejection in Coadd
  --MWM_fluxer, --mwm
  --map3d {bayestar15,bay15,merge3d}
                        Name of 3d dustmap to use with MWM_fluxer
                        (default=bayestar15)
  --no_healpix, --nohp  Turn off copy to healpix
  --noxcsao             Skip pyXCSAO
  --skip_specprimary    Skip Calculation of Specprimary
  --no_merge_spall      Skip building full SpAll File
  --skip2d              Skip spreduce2d
  --only1d              run spec1d step only (eg. spreduce1d_empca, XCSAO)
  --onestep_coadd       Use legacy one step version of coadd
  --fibermap_clobber    Clobber spfibermap fits file
  --saveraw             Save sdssproc outputs
  --debug               Save extraction debug files
  --no_db               skip Database operations
  --fast_no_db FAST_NO_DB
                        When using --no_db, streamlines process and only gets
                        parallax from MOS target files
  --sdss_access_release SDSS_ACCESS_RELEASE
                        sdss_access data release (defaults to sdsswork),
                        required if you do not have proprietary access,
                        otherwise see https://sdss-
                        access.readthedocs.io/en/latest/auth.html#auth
  --sdss_access_remote  allow for remote access to data using sdss-access
  --dr19                Limit targeting flags to DR19 cartons
  --a2t                 Force Use of Arc2Trace

Select Fields:
  --fieldids [FIELDIDS [FIELDIDS ...]], -f [FIELDIDS [FIELDIDS ...]]
                        Plate/Field numbers to reduce default="*"
  --fieldstart FIELDSTART
                        Starting Field/Plate number
  --fieldend FIELDEND   End Field/Plate number

Select MJDs:
  --mjd [MJD [MJD ...]], -m [MJD [MJD ...]]
                        MJD dates to reduce; default="*"
  --mjdstart MJDSTART   Starting MJD
  --mjdend MJDEND       Ending MJD

Slurm Options:
  --no_write            skip writing and submitting job
  --shared              Node sharing
  --fast                Use SDSS fast queue
  --mem_per_cpu MEM_PER_CPU
                        Memory allocated per CPU
  --walltime WALLTIME   Wall time in hours
  --nodes NODES         Number of Nodes
  --ppn PPN             Number of processors per node
  --nosubmit            Build, but not submit redux files
  --clobber             Clobber redux

Custom Coadd Options:
  --epoch               Epoch Coadds
  --custom CUSTOM       Name of custom Coadd Schema
  --allsky              All Sky Coadds
  --coadd_only          Run spspec_target_merge only
  --1dpost              Run 1d analysis and post processing only

Email outputs:
  --email               Email log using $HOME/daily/etc/emails
uurundaily

^^^^^^^^^^
 usage: uurundaily [-h] [--apo] [--lco] [--module MODULE]
                  [--mjd [MJD [MJD ...]]] [--range_mjd RANGE_MJD] [--clobber]
                  [--fast] [--saveraw] [--debug] [--skip_plan] [--nosubmit]
                  [--noslurm] [--batch] [--nodb] [--epoch] [--summary]
                  [--monitor] [--pause PAUSE] [--merge3d] [--traceflat]
                  [--no_prep] [--no_dither]

Process the BOSS data for a single MJD end-to-end (including plan files)

optional arguments:
  -h, --help            show this help message and exit
  --apo
  --lco
  --module MODULE       Module for daily run
  --mjd [MJD [MJD ...]]
                        Manually run for a single/list of mjd (does not update
                        nextmjd.par)
  --range_mjd RANGE_MJD
                        Manually run for a range of mjds (does not update
                        nextmjd.par)
  --clobber             clobber uubatchpbs run
  --fast                turn on fast user for slurm
  --saveraw             save sdssproc outputs
  --debug               save extraction debug files
  --skip_plan           Skip createing spplan files
  --nosubmit            Skip submitting uubatch job (ideal for allowing
                        editting of plans)
  --noslurm             Skip creating uubatch job
  --batch               run for multiple mjds in a single batch
  --nodb                skip Database operations
  --epoch               Run Epoch Coadds
  --summary             Build Summary Files
  --monitor             Monitors pipeline status
  --pause PAUSE         Pause time (s) in status updates
  --merge3d             Use prototype 3D Dustmap (in merge mode)
  --traceflat           Build and use TraceFlats
  --no_prep             Skip building TraceFlats and spfibermaps before
                        pipeline run
  --no_dither           Skip Dither Engineering Fields
.. End of document

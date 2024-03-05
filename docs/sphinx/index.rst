.. title:: IDLspec2D: The SDSS BOSS Data Reduction Pipeline

IDLspec2D: The SDSS BOSS Data Reduction Pipeline
====================
This page describes the BOSS Data Reduction Pipeline `idlspec2d <https://github.com/sdss/idlspec2d>`.


The BOSS DRP (officially known as IDLspec2D) is really a series of steps run in sequence. There are some initial steps to produce the plans and supplementary information required. After which, uubatchpbs is used to produce the redux scripts. These scripts are really a wrapper script designed to run each of the individual steps on a field-mjd basis by the slurm manager at CHPC (Utah) or manually on any computer. Starting with the v6_2_x version of the pipeline, the internal python commands have been organized into a boss_drp package within the IDLspec2D GitHub repo.

The Pipeline can be run in various ways, where the catchup method is designed to run a large number of MJDs in a short time and the daily run method is designed to run for 1 (or a few) MJDs.

.. contents:: **Table of Contents**


Major changes since version v6_1_X
-----------------------------

The idlspec2d package received a cleanup of old unused scripts and reorganized the internal python functions into an internal boss_drp python package



Directory Contents
------------------

* **bin**:
* **catfiles**:
* **datamodel**:
* **docs**:
* **etc**:
* **examples**:
* **include**:
* **lib**:
* **Makefile**:
* **opfiles**:
* **pro**:
* **python**:
* **src**:
* **templates**:
* **ups**:





.. _packaging-section-v2:

Setup Requirements
-------------------

A number of system environmental variables and paths are required to run the BOSS DRP.

Running at the University of Utah CHPC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

At Utah, modules (github.com/sdss/sdss_modules) are used to maintain the the required packages and paths. For the BOSS pipeline, the bhm modules are used to manage these for the BOSS pipeline.

Environmental Variables
^^^^^^^^^^^^^^^^^^^^^^^

export DATABASE_PROFILE="pipelines"
export RUN2D="v6_1_2"
export RUN1D="v6_1_2"
export BOSS_SPECTRO_REDUX="/uufs/chpc.utah.edu/common/home/sdss50/sdsswork/bhm/boss/spectro/redux"
export SDHDRFIX_DIR="/uufs/chpc.utah.edu/common/home/sdss50/software/git/sdss/sdsscore_test/main"
export IDLSPEC2D_DIR="/uufs/chpc.utah.edu/common/home/sdss50/software/git/sdss/idlspec2d/$RUN2D"
export SDSSCORE_DIR="/uufs/chpc.utah.edu/common/home/sdss50/software/git/sdss/sdsscore_test/main"

Paths
^^^^^

export IDL_PATH="$IDL_PATH:$IDLSPEC2D_DIR"
export PATH="$PATH:$IDLSPEC2D_DIR/bin"
export PYTHONPATH="$PYTHONPATH:$IDLSPEC2D_DIR/python"

Dependencies
^^^^^^^^^^^^

* idl
* python(3.7-3.9)
* SDSS Collaboration Package Dependencies
    * idlutils: idlutils is a collection of IDL functions and routines used by a variety of SDSS software.
    * sdssdb: sdssdb contains the source catalogs, targeting catalogs, and operational databases.
    * semaphore: provides codes and reference files to decode and understand the sdss_target_flags
    * sdss-tree: provides environment variables to manage paths for SDSS data as they organized on the Science Archive Server (SAS)
    * sdss_access: provides a convenient way of navigating local and remote file system paths from the Science Archive Server (SAS)
    * pyVista:
    * SDSS Slurm: Required for use of uurundaily at Utah, all other command can be manually (at Utah or elsewhere) run without access to the slurm manager provided by this package
    * SDSS Product Dependencies
    * elodie: A database of high and medium-resolution stellar spectra (Prugniel+, 2001) used by spec1d to classify spectra and determine stellar parameters.
    * dust: A catalog of dust extinction models, including the SFD model.
    * speclog: speclog is an SDSS product that contains information about SDSS BOSS plate operations including seeing measured by the guides (guiderMon-{MJD}.par, plate plug maps (plPlugMapM-{plateid}-{mjd}-{plugid}.par, and plate header correction files to change the header exposure values (sdHdrFix-{mjd}.par)
    * platelist: platelist is an SDSS product that contains information on the plate designs and plugging. The plateHoles files include additional metadata associated with the targets on a plate
    * specflat: specflat is an SDSS product that contains master calibration frames and bad pixel masks for use in the idlspec2d pipeline.
    * gaia/dr2: idlspec2d utilizes gaia_source/csv to calculate the distance to standard stars from GAIA DR2 proper motion.
* External Dependencies
    * pyDL: a package that consists of python replacements for IDL function, both built-in and from external astronomical libraries
    * dustmaps: provides a unified interface for several 2D and 3D maps of interstellar dust reddening and extinction. idlspec2d makes use of the Bayestar 2015 dustmaps (Green, Schlafly, Finkbeiner et al. 2015)
    * PyXCSAO: a python package designed to replicate the functionality of IRAF XCSAO.
    * numpy: a standard Python package for arrays and high-level mathematical functions
    * astropy: a collection of astronomy packages written in Python
    * matplotlib: a python plotting library
    * healpy: a Python package based on the Hierarchical Equal Area isoLatitude Pixelization (HEALPix) scheme
    * tqdm: a progress bar for Python
    * pandas: a python package designed for data manipulation and analysis
    * h5py: a python interface between numpy and HDF5 data
    * scipy: a python package for scientific and technical computing
    * pillow: a python image file processing library
    * termcolor: a python package for color formatting of terminal outputs (not required but recommended)



.. toctree::
    :hidden:

    v1/v1
    standards
    changelog

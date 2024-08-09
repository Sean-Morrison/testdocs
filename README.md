# idlutils

A collection of IDL functions and routines used by a variety of SDSS software.

## Should I be using the SVN version instead?

Until the end of SDSS-IV `idlutils` is maintained as a [SVN repository](https://trac.sdss.org/browser/repo/sdss/idlutils) and a GitHub repo (this one). SVN development happens as `v5_x`, while Git development uses the `6.x` series. The SVN `trunk` and the GitHub `master` branches will **not** synced until the end of SDSS-IV. `v5` tags are synced from SVN to GitHub every now and then. The `6.0.0` tag introduces breaking changes (see below).

So, what version should you be using? If you're developing SDSS-IV software (e.g., `mangadrp`, or the `apogee` pipeline), you probably want to keep using the `v5` branch and do your changes in SVN. If you're developing for SDSS-V you *should* be using the `6.x` tags and develop against the GitHub repository.

## External libraries

Version 6.x does not ship with the [Goddard](https://github.com/wlandsman/IDLAstro) and [Coyote](https://github.com/idl-coyote/coyote) libraries but `idlutils` still depends on them. You need to make sure that they are available in your `IDL_PATH`. Alternatively, you can use [sdss_install](https://github.com/sdss/sdss_install) to checkout a copy of `idlutils` while also installing Coyote and the Goddard libraries as modules.

## Installing idlutils
To install idluils locally run:

```
git clone https://github.com/sdss/idlutils.git idlutils
```

This will download the master branch, where active development occurs. To retrieve recent changes after downloading the repo, use git pull.
Version 6.2.0 is recommended for use with DR18 data. To retrieve this tag use `git checkout 6.2.0`. To list other available tags, use the command `git tag`.
> [!NOTE]
> These access points are read-only! If you want to develop or add to the idlutils software you must be an SDSS collaborator.

### Prerequisites
You do not need to install IDL, buy a license, etc. to install idlutils. However, you do need a copy of IDL’s export.h file. If you already have IDL installed, set the environment variable IDL_DIR to the directory containing the external directory. The external directory should contain the export.h file. If you do not have IDL installed, but do have an export.h file, then you can place that file in a directory called external then place that directory in any directory you want and set IDL_DIR to the directory containing external.

> [!NOTE]
> You need both a C compiler and a Fortran compiler.

If you want to build the documentation, you must have IDL installed, and the executable idl must live somewhere in your PATH. Note that some IDL installations define the executable idl as a shell alias, and thus it will not be in your PATH.

### Compilation

After exporting or checking out the code, set the environmental variable `IDLUTILS_DIR` to the location of your idlutils directory. Then set the variables:
```
export PATH=$IDLUTILS_DIR/bin:$PATH
export IDL_PATH=+$IDLASTRO_DIR/pro:+$IDLCOYOTE_DIR:+$IDLUTILS_DIR/pro:$IDL_PATH
```
where `$IDLASTRO_DIR` is where you installed the [Goddard](https://github.com/wlandsman/IDLAstro) library and `$IDLCOYOTE_DIR` is where you installed the [Coyote](https://github.com/idl-coyote/coyote) library.

Of course, you should put those commands into your .bash_profile or (suitably modified) into your .tcshrc file where appropriate.

To build the code, execute:

```
cd $IDLUTILS_DIR; evilmake all
```

This will build all of the C libraries.

To build the documentation (see the Prerequisites above), execute:

```
cd $IDLUTILS_DIR; evilmake all
```

## Versioning

Version 6.0.0 is the first one using `X.Y.Z.` instead of the previous `vX_Y_Z` syntax. If your product does idlutils version parsing you may need to update your code to handle both types of version string.

We use [bumpversion](https://github.com/peritus/bumpversion) to set the current version of idlutils. This replaces the previous system that used SVN variable substitution, which was deprecated with the migration to GitHub.

To install `bumpversion` run

```
pip install bumpversion
```

If, for example, the current version is `6.1.1` and you want to updte the minor version to `6.2.0` do `bumpversion minor` which will set the version to `6.2.0dev`. You can also modify the `major` or `patch` sections of the version. When you're ready to tag the product, run `bumpversion release` to remove the `dev` suffix. DO NOT MODIFY FILE VERSIONS DIRECTLY. For more information, read [this](https://sdss-python-template.readthedocs.io/en/latest/#bumpversion-section).

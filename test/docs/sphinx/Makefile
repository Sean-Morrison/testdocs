# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = /Users/smorrison/opt/anaconda3/bin/python3.8 -msphinx
SPHINXPROJ    = BMO
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".


help:
	@/Users/smorrison/opt/anaconda3/bin/python3.8 ../build_doc.py
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@/Users/smorrison/opt/anaconda3/bin/python3.8 ../build_doc.py
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

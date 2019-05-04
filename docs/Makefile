# Minimal makefile for Sphinx documentation
#
VERSION=$(strip $(shell cat ../version))
# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

all:
	@aws s3 sync ./build/html s3://docs.arcblock.io/forge-sdk/python/latest --region us-west-2 --profile prod
	@aws s3 sync ./build/html s3://docs.arcblock.io/forge-sdk/python/$(basename $(VERSION)) --region us-west-2 --profile prod


.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

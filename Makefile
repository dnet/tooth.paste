.PHONY: docs build test coverage pylint flake8 pep8 pyflakes package dotpackage dotdotpackage examplepackage exampledotpackage exampledotdotpackage diff sloccount dryrelease mkrelease

ifndef VTENV_OPTS
VTENV_OPTS = "--no-site-packages"
endif

docs: bin/sphinx-build
	SPHINXBUILD=../bin/sphinx-build $(MAKE) -C docs html $^

build:	
	virtualenv $(VTENV_OPTS) .
	bin/python setup.py develop

test: bin/nosetests
	bin/nosetests -s tooth/paste

coverage: bin/coverage bin/nosetests
	bin/nosetests --with-coverage --cover-html --cover-html-dir=html --cover-package=tooth.paste
	bin/coverage html

pylint:	bin/pylint
	bin/pylint -i y tooth/paste

flake8:	bin/flake8
	bin/flake8 --max-complexity 12 tooth/paste

pep8:	bin/pep8
	bin/pep8 tooth/paste

pyflakes:	bin/pyflakes
	bin/pyflakes tooth/paste

package: bin/python
	# Hack to make believe templer that the current folder is the home folder
	# so that it reads the local .zopeskel file with the defaults
	./bin/templer package

dotpackage: bin/python
	# Hack to make believe templer that the current folder is the home folder
	# so that it reads the local .zopeskel file with the defaults
	./bin/templer dotpackage

dotdotpackage: bin/python
	# Hack to make believe templer that the current folder is the home folder
	# so that it reads the local .zopeskel file with the defaults
	./bin/templer dotdotpackage

examplepackage: bin/python
	# Hack to make believe templer that the current folder is the home folder
	# so that it reads the local .zopeskel file with the defaults
	export OLDHOME="${HOME}"; export HOME="${PWD}"; ./bin/templer package examplepackage; export HOME="${OLDHOME}"

exampledotpackage: bin/python
	# Hack to make believe templer that the current folder is the home folder
	# so that it reads the local .zopeskel file with the defaults
	export OLDHOME="${HOME}"; export HOME="${PWD}"; ./bin/templer dotpackage example.dotpackage; export HOME="${OLDHOME}"

exampledotdotpackage: bin/python
	# Hack to make believe templer that the current folder is the home folder
	# so that it reads the local .zopeskel file with the defaults
	export OLDHOME="${HOME}"; export HOME="${PWD}"; ./bin/templer dotdotpackage example.dotdot.package; export HOME="${OLDHOME}"

diff: bin/python
	# Show the difference between the current package and the regenerated one
	colordiff -c -r tooth.paste .|less -r

sloccount:	bin/python
	sloccount tooth/paste

dryrelease:	bin/mkrelease
	bin/mkrelease --no-commit --no-tag --dry-run -d pypi

mkrelease:	bin/mkrelease
	bin/mkrelease --no-commit --no-tag  -d pypi

bin/sphinx-build: bin/python
	bin/pip install sphinx
	bin/pip install coverage

bin/nosetests: bin/python
	bin/pip install nose

bin/coverage: bin/python
	bin/pip install coverage

bin/pylint: bin/python
	bin/pip install pylint

bin/flake8: bin/python
	bin/pip install flake8

bin/pyflakes: bin/python
	bin/pip install pyflakes

bin/pep8: bin/python
	bin/pip install pep8

bin/mkrelease: bin/python
	bin/pip install jarn.mkrelease

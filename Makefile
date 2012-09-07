.PHONY: docs build test coverage pylint flake8 templer

ifndef VTENV_OPTS
VTENV_OPTS = "--no-site-packages"
endif

docs: bin/sphinx-build
	SPHINXBUILD=../bin/sphinx-build $(MAKE) -C docs html $^

build:	
	virtualenv $(VTENV_OPTS) .
	bin/python setup.py develop

test: bin/nosetests
	bin/nosetests -s tooth.paste

coverage: bin/coverage bin/nosetests
	bin/nosetests --with-coverage --cover-html --cover-html-dir=html --cover-package=tooth.paste
	bin/coverage html

pylint:	bin/pylint
	bin/pylint thooth/paste

flake8:	bin/flake8
	bin/flake8 --max-complexity 12 tooth/paste

templer: bin/python
	# Hack to make believe templer that the current folder is the home folder
	# so that it reads the local .zopeskel file with the defaults
	export HOME="${PWD}"; ./bin/templer tooth_basic_namespace tooth.paste
	# Show the difference between the current package and the regenerated one
	colordiff -c -r tooth.paste .|less -r

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

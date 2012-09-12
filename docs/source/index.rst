Tooth.paste: Shiny new Python packages!
=======================================

Tooth.paste creates shiny new Python packages. Start your new packages with a prepared
Sphinx documentation section, a test folder for your unit tests and a Makefile containing
all the tools needed to keep your Python code clean.


Get started
-----------

Prepare everything for development

    $ cd tooth.paste
    $ virtualenv --no-site-packages .
    $ bin/python setup.py develop


Creating a new package
----------------------

Create shiny new Python package:

    $ ./bin/templer tooth_basic_namespace my.project

Get started with the new package
--------------------------------

    cd my.project
    make build

Document your package
---------------------

Write some documentation:

    docs/source/index.rst

Build the html Sphinx documentation
-----------------------------------

Run the following make command:

    make docs

The HTML documentation is available here:

    docs/build/html/index.html 

Write some code
---------------

You can start adding code:

    cd my/project
    vim __init__.py

Write some tests
----------------

You can start adding code:

    cd tests
    vim test_project.py

Run the tests
-------------

    make test

Run the coverage
----------------
   
    make coverage

You can then have a look at the coverage in the generated HTML pages:

    htmlcov/index.html

Run pylint
----------
 
    make pylint

Run flake8
----------

    make flake8

Run pep8:
---------

    make pep8


Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

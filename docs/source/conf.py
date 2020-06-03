# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


import os
import sys
from configparser import RawConfigParser
import sphinx_rtd_theme


# -- Project information -----------------------------------------------------

project = 'Modern Identity for Developers'
copyright = '2020 Microsoft'
author = 'Ronny.Hansen@Microsoft.com'

# The full version, including alpha/beta/rc tags
release = '1.2.6'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark', 'sphinx_rtd_theme']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_logo = '_static/logo.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,    
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# If you have your own conf.py file, it overrides Read the Doc's default conf.py. 
# By default, Sphinx expects the master doc to be contents. Read the Docs will 
# set master doc to index instead (or whatever it is you have specified in your settings). 
# Try adding this to your conf.py:

master_doc = 'index'
import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "broken_symlink_dir_demo",
    version = "0.0.1",
    author = "Matthew Goodman",
    author_email = "matt@3scan.com",
    description = ("Showing a broken behavior."),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['BrokenPackage'],
    long_description=read('README.md'),
)

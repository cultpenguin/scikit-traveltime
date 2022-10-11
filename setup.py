"""Traveltime computation based on scikit-fmm
See:
https://github.com/cultpenguin/scikit-traveltime
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.


from distutils.core import setup
setup(
    name = 'scikit-traveltime',
    version = '0.1.0',
    description = 'Traveltime computation based on the fast marching method for solving the eikonal equation',
    author = 'Thomas Mejer Hansen',
    author_email = 'thomas.mejer.hansen@gmail.com',
    url = 'https://github.com/cultpenguin/scikit-traveltime', # use the URL to the github repo
    download_url = 'https://github.com/cultpenguin/scikit-traveltime/archive/master.zip', # I'll explain this in a second
    keywords = ['traveltime', 'eikonal', 'fast-marching'], # arbitrary keywords
    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']), # Required
    install_requires=['numpy >= 1.0.2', 'scipy >= 1.0.0', 'scikit-fmm >= 0.0.9'],
)


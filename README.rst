scikit-traveltime: traveltime calculation using the fast marching method for Python
===================================================================================

.. image:: https://img.shields.io/pypi/v/scikit-traveltime.svg?style=flat-square
    :target: https://pypi.org/project/scikit-traveltime

.. image:: https://img.shields.io/pypi/pyversions/scikit-traveltime.svg?style=flat-square
    :target: https://pypi.org/project/scikit-traveltime

.. image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
    :target: https://en.wikipedia.org/wiki/MIT_License

.. code:: 

   import numpy as np
   import traveltime as tt
   
   #%% CREATE REFERENCE VELOCITY MODEL
   dx=0.1;
   x = np.arange(-1,6,dx)
   y = np.arange(-1,13,dx)
   V=0.1*np.ones((len(y),len(x)))
   
   #%% SET SOURCE AND RECEIVERS
   S=np.array([[0,2],[0,5],[0,4]])
   R=np.array([[5,12],[5,5],[5,1]])
   
   t = tt.eikonal_traveltime(x,y,[],V,S,R)
       

Documentation
--------------

PyPI
~~~~~~~~~~~
`<http://pypi.python.org/pypi/scikit-traveltime>`

Requirements
~~~~~~~~~~~~
* numpy >= 1.0.2
* scipy >= 1.0.0
* scikit-fmm >= 1

Bugs, questions, patches, feature requests, discussion & cetera
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* Open a GitHub pull request or a GitHub issue

Installing
~~~~~~~~~~
* Via pip: `pip install scikit-traveltime`

Version History:
~~~~~~~~~~~~~~~~
* 0.0.1: July 1st, 2017
* 0.0.4: January 3rd, 2017
* 0.1.0: November 11, 2022 (cleanup)
* 0.1.2: March 19, 2025 (depreceted use of interp2d, moved to pyproject.toml)
  
Copyright 2022 Thomas Mejer Hansen

See LICENSE (MIT) in the source directory.

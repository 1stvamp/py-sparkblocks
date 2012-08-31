py-sparkblocks
==============

About sparkblocks
-----------------
``sparkblocks`` is a Python module that provides a single function, ``spark()`` which takes a list of numbers (ints or floats) and outputs a string containing a unicode character (9601-9608) sparklines bargraph representation of the numbers.

It is based on the `spark tool <https://github.com/holman/spark>`_ by Zach Holman, and the original `Twitter sparkline generator <http://www.datadrivenconsulting.com/2010/06/twitter-sparkline-generator/>`_ by Alex Kerin.

Installation
------------
The library can be installed from PyPi using ``pip``::

    pip install py-sparkblocks

Or cloned from `Github <http://www.github.com/>`_ using ``git``::

    git clone git://github.com/1stvamp/py-sparkblocks.git
    cd py-sparkblocks
    python setup.py install

Usage
-----

    >>> from sparkblocks import spark
    >>> print(spark([1, 2, 0.2, 3.1, 2]))
    ▂▅▁▇▅

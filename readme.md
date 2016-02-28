bz2_rl
======

[![PyPI version](https://badge.fury.io/py/bz2_rl.svg)](https://pypi.python.org/pypi/bz2_rl)

**Helper class for processing large bzip2 compressed text files efficiently
without high memory usage.**

I originally wrote this class to help me run through a large SQL dump
which was over 90 MB uncompressed. This class basically just wraps the
streaming bzip2 decompressor from the standard library in an iterator,
making it very easy to run through the lines of a compressed file
without actually loading the file into memory.

This is specifically built for *text* files.

Tested with Python 3.5, but should work for all Python 3 versions.


Installation and usage
----------------------

Install using `pip`, e.g.

    $ pip install bz2_rl

Or add it as dependency to your own project's `setup.py`.


Development
-----------

I'm always glad to accept pull requests or to look at issues or questions.

### Tests

Run `./setup.py test` to run the unit tests.


License
-------

MIT licensed.

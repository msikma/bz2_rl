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


Installation
------------

Install using `pip`, e.g.

    $ pip install bz2_rl

Or add it as dependency to your own project's `setup.py`.


Usage
-----

Usage is very simple: make an instance with at least the path to the file
as argument, then iterate over it. For example:

    from bz2_rl import BZ2FileIter
    sql_lines = BZ2FileIter('exports/database.sql')
    for line in sql_lines:
        # ...

The following arguments are supported:

* `encoding` - specifies encoding of the compressed text (default: `utf-8`)
* `read_size` - amount of bytes to read per iteration (default: 512)
* `linebreak` - turns off linebreak auto-detection and forces a specific type (default: None)

Linebreaks are auto-detected and converted to the system default.

The file is closed automatically after the last line. If you don't need
to use the file anymore, simply delete the `BZ2FileIter` instance
to close the file.


Development
-----------

I'm always glad to accept pull requests or to look at issues or questions.

### Tests

Run `./setup.py test` to run the unit tests.


License
-------

MIT licensed.

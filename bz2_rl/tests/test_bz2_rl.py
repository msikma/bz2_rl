# (C) 2016, MIT License

import unittest
import itertools
from os import path
from ..bz2_rl import BZ2TextFileStreamer


class TestConverter(unittest.TestCase):
    '''
    Run this using ./setup.py test
    '''
    def setUp(self):
        '''
        Initialize the KanaConverter.
        '''
        cwd = path.dirname(path.realpath(__file__))

        self.path_txt = '{}/test.txt'.format(cwd)
        self.path_bz2 = '{}/test.txt.bz2'.format(cwd)
        self.bz2de = BZ2TextFileStreamer(self.path_bz2)

    def test_bz2de(self):
        '''
        Tests whether decompressed lines from a bzip2 file match the
        original, non-compressed lines precisely.
        '''
        # Since the file is Unicode, it doesn't need decoding.
        with open(self.path_txt, 'r') as file_txt:
            lines_txt = itertools.chain(file_txt.readlines())

        for line in self.bz2de:
            self.assertEqual(next(lines_txt), line)

        # Note: this is by no means an exhaustive test, but it's a start.

if __name__ == '__main__':
    unittest.main()

# (C) 2016, MIT License

import unittest
from ..bz2_rl import BZ2TextFileStreamer


class TestConverter(unittest.TestCase):
    '''
    Run this using ./setup.py test
    '''
    def setUp(self):
        '''
        Initialize the KanaConverter.
        '''
        self.bz2de = BZ2TextFileStreamer()

    def test_bz2de(self):
        '''
        asdf
        '''
        self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()

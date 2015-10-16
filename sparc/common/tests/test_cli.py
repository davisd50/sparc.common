"""Test
"""
import unittest
from doctest import DocTestSuite
from doctest import DocFileSuite

import sparc.common

def test_suite():
    return unittest.TestSuite((
        DocFileSuite('cli.txt',
                     package=sparc.common),))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
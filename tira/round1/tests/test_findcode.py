import unittest
from findcode import find_code
from findcode import Oracle
import itertools
import random

class TestFindCode(unittest.TestCase):
    # test all possible codes
    def test_all_codes(self):
        print("\nTesting 1000 random codes")
        test_codes = [''.join(p) for p in itertools.permutations('123456789', 4)]
        test_codes = random.sample(test_codes, 1000)
        for code in test_codes:
            oracle = Oracle(code)
            self.assertEqual(find_code(oracle), code)
        


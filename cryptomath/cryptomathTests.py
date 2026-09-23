import unittest
from gcd import findGCD


#test cases for base gcd function
#test case 1: tests for two positive numbers
#test case 2: tests for two negative numbers
class gcdTest(unittest.TestCase):
    def test_gcd_pos(self):
        self.assertEqual(findGCD(4883,4369), 257)
    def test_gcd_neg(self):
        self.assertEqual(findGCD(-4883,-4369), 257)


unittest.main()
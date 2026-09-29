import unittest
from gcd import findGCD
from exgcd import findExGCD
from modInverse import findModInv

#test cases for base gcd function
#test case 1: tests for two positive numbers
#test case 2: tests for two negative numbers
#all test cases for findGCD pass
class gcdTest(unittest.TestCase):
    def test_gcd_pos(self):
        self.assertEqual(findGCD(4883,4369), 257)
    def test_gcd_neg(self):
        self.assertEqual(findGCD(-4883,-4369), 257)
#test cases for extended euclidian gcd
#test case 1: tests the extended gcd with 35 and 15
class exgcdTest(unittest.TestCase):
    def test_exgcd(self):
        self.assertEqual(findExGCD(35, 15), (5, 1, -2))

#test cases for mod inverse
#test case 1: tests the mod inverse function with 3 and 11
class modInvTest(unittest.TestCase):
    def test_modInv(self):
        self.assertEqual(findModInv(3, 11), 4)

unittest.main()
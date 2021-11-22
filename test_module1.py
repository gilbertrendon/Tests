#from sample_module/sample_tests import add2num
#from sample_module import sample_tests
from sample_module.sample_module import add2num,pow2num

import unittest
class Testadd2num(unittest.TestCase):
    @classmethod
    def test_setUpClass(cls):
        print('Executed before any test in the class runs.')
    @classmethod
    def test_tearDownClass(cls):
        print('Executed after all tests in class are run.')
    def test_setUp(self):
        print('Executed before start of every test')
    def test_tearDown(self):
        print('Executed at the end of every test')
    def test_sum_2pos_num(self):
      self.assertEqual(add2num(6, 7), 13)
    def test_sum_1pos_and_1neg_num(self):
      self.assertEqual(add2num(-10, 9), -1)

class Testpow2num(unittest.TestCase):

    def test_pow_2pos_num(self):
        self.assertEqual(pow2num(3, 4), 81)

    def test_neg_pow(self):
        self.assertEqual(pow2num(10, -2), 0.01)

    def test_negnum_pow(self):
        self.assertEqual(pow2num(-3, 3), -26)
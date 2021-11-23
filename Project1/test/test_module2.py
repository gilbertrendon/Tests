from proj.sample_module import add2num

import unittest


class SampleTestClass(unittest.TestCase):

    def test_sample1(self):
      with self.assertRaises(TypeError) as e:
            r = add2num(3, 'hello')
      self.assertEqual(str(e.exception), "unsupported operand type(s) for +: 'int' and 'str'")




#       import unittest

# class SampleTestClass(unittest.TestCase):

#     def sample_test1(self):
#         self.assertEqual('HELLO', 'hello'.upper())

#     def test_sample2(self):
#         self.assertEqual(3*3, 9)
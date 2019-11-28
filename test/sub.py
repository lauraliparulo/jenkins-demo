import unittest

from sum import *

class TestSum(unittest.TestCase):

    def test_sub_1(self):
        self.assertEqual(subtract_numbers(3,2), 1, "expected sub of 3 and 2 to be 1 but got " + str(subtract_numbers(1,2)))

    def test_sum_2(self):
        self.assertEqual(subtract_numbers(10,20), -10, "expected sub of 10 and 20 to be -10 but got " + str(subtract_numbers(10,20)))

    def test_sum_3(self):
        self.assertEqual(subtract_three_numbers(10,20,30), -60, "expected sub of 10, 20 and 30 to be 60 but got" + str(subtract_three_numbers(10,20,30)))

if __name__ == "__main__":
    unittest.main()

"""
Author: Edward
10/29/20
Saw this and thought it should be in it's own file.
"""
import unittest
from main import marriedPercentage
from main import negative

#printWhole(text_file)
#sprintOneTestFunctionOne()
class TestStringMethods(unittest.TestCase):
    # test function to test equality of two value
    def test_negative(self):
        g = float(8/9)
        firstValue = g
        secondValue = marriedPercentage()
        # error message in case if test case got failed
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(firstValue, secondValue, message)


if __name__ == '__main__':
    unittest.main()

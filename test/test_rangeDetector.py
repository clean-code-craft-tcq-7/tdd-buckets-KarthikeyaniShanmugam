import unittest

from src import rangeDetector


class validateTester(unittest.TestCase):
    def test(self):  
        self.assertTrue(rangeDetector.detectRange([3, 3, 4, 5, 10, 11, 12]) == [[3,3,4,5],[10,11,12]])
        self.assertTrue(rangeDetector.detectRange([100,101,102,500,501,501,502,503]) == [[100,101,102],[500,501,501,502,503]])
        self.assertTrue(rangeDetector.detectRange([1,1,1,1,3,3,3,3]) == [[1,1,1,1],[3,3,3,3]])

if __name__ == '__main__':
    unittest.main()
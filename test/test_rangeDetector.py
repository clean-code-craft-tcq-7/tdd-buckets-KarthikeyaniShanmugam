import unittest
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath('src'))
CURRENT_DIR = os.path.join(CURRENT_DIR,'src')
sys.path.append(os.path.dirname(CURRENT_DIR))
from src import rangeDetector


class validateTester(unittest.TestCase):
    def test(self):  
        self.assertTrue(rangeDetector.detectRange([3, 3, 4, 5, 10, 11, 12]) == [[3,3,4,5],[10,11,12]])
        self.assertTrue(rangeDetector.detectRange([100,101,102,500,501,501,502,503]) == [[100,101,102],[500,501,501,502,503]])
        self.assertTrue(rangeDetector.detectRange([1,1,1,1,3,3,3,3]) == [[1,1,1,1],[3,3,3,3]])

if __name__ == '__main__':
    unittest.main()
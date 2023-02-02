import unittest
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath('src'))
CURRENT_DIR = os.path.join(CURRENT_DIR,'src')
sys.path.append(os.path.dirname(CURRENT_DIR))
from src import sorter


class validateTester(unittest.TestCase):
    def test(self):  
        self.assertTrue(sorter.getSort([3, 3, 5, 4, 10, 11, 12]) == [3, 3, 4, 5, 10, 11, 12])
        self.assertTrue(sorter.getSort([-1,-3,-2]) == [-3,-2,-1])
if __name__ == '__main__':
    unittest.main()
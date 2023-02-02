import unittest
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath('src'))
CURRENT_DIR = os.path.join(CURRENT_DIR,'src')
sys.path.append(os.path.dirname(CURRENT_DIR))
from src import rangeAndReadingsFinder


class validateTester(unittest.TestCase):
    def test(self):  
        self.assertTrue(rangeAndReadingsFinder.range_and_readings_counter([3, 3, 5, 4, 10, 11, 12]) == [[3,5,4],[10,12,3]])
        self.assertTrue(rangeAndReadingsFinder.range_and_readings_counter([100,101,102,500,501,501,502,503]) == [[100,102,3],[500,503,5]])
        self.assertTrue(rangeAndReadingsFinder.range_and_readings_counter([1,1,1,1,3,3,3,3]) == [[1,1,4],[3,3,4]])
        self.assertTrue(rangeAndReadingsFinder.range_and_readings_counter([]) == [])
        self.assertTrue(rangeAndReadingsFinder.range_and_readings_counter([0]) == [])
if __name__ == '__main__':
    unittest.main()
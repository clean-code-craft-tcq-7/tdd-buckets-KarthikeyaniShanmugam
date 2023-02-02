import unittest
import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath('src'))
CURRENT_DIR = os.path.join(CURRENT_DIR,'src')
sys.path.append(os.path.dirname(CURRENT_DIR))
from src import rangeDetector


class RangeTester(unittest.TestCase):
    # Returns True or False. 
    def test(self): 
        detector = rangeDetector.RangeDetector()      
        self.assertTrue(detector.range_and_readings_counter([3, 3, 5, 4, 10, 11, 12]) == [[[3,5], 4],[[10,12], 3]])
        self.assertTrue(detector.range_and_readings_counter([4,5]) == [[[4,5],2]])
if __name__ == '__main__':
    unittest.main()
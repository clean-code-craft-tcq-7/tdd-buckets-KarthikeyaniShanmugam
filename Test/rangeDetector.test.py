import sys
sys.path.append('Source')


import unittest

from Source import rangeDetector


class RangeTester(unittest.TestCase):
    # Returns True or False. 
    def test(self): 
        detector = rangeDetector.RangeDetector()      
        self.assertTrue(detector.range_and_readings_counter([3, 3, 5, 4, 10, 11, 12]) == [[[3,5], 4],[[10,12], 3]])
        self.assertTrue(detector.range_and_readings_counter([4,5]) == [[[4,5],2]])
if __name__ == '__main__':
    unittest.main()
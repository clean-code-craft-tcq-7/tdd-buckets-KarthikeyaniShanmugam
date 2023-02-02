import unittest

from src import rangeCounter


class validateTester(unittest.TestCase):
    def test(self):  
        self.assertTrue(rangeCounter.counter([3,3,4,5]) == [3,5,4])
        self.assertTrue(rangeCounter.counter([100,101,102]) == [100,102,3])
        self.assertTrue(rangeCounter.counter([1,1,1,1]) == [1,1,4])

if __name__ == '__main__':
    unittest.main()
import unittest
#import os, sys
#CURRENT_DIR = os.path.dirname(os.path.abspath('src'))
#CURRENT_DIR = os.path.join(CURRENT_DIR,'src')
#sys.path.append(os.path.dirname(CURRENT_DIR))
from src import validator


class validateTester(unittest.TestCase):
    def test(self):  
        self.assertTrue(validator.getValidation([3, 3, 5, 4, 10, 11, 12]) == True)
        self.assertTrue(validator.getValidation([]) == False)
        self.assertTrue(validator.getValidation([0]) == False)
        self.assertTrue(validator.getValidation([-1]) == False)
if __name__ == '__main__':
    unittest.main()
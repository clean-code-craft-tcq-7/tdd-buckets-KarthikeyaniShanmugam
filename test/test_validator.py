import unittest

from src import validator


class validateTester(unittest.TestCase):
    def test(self):  
        self.assertTrue(validator.getValidation([3, 3, 5, 4, 10, 11, 12]) == True)
        self.assertTrue(validator.getValidation([]) == False)
        self.assertTrue(validator.getValidation([0]) == False)
        self.assertTrue(validator.getValidation([-1]) == False)
if __name__ == '__main__':
    unittest.main()
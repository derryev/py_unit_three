import unittest
#import file you want to test
import return_addition.py

#every tests starts with a class definition, you want to have organization around properties of the function
#things after a peropd are a property of a specific method or function
class MyTestCase(unittest.TestCase):
    def test_return_addition(self):
        self.assertEqual(15, return_addition.add_two(7,8))
        pass


if __name__ == "__main__":
    unittest.main()
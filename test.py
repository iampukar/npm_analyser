import unittest
from src.npm_analyser.npm_analyser import npm_analyser

class Test(unittest.TestCase):
    def test_cases(self):
        """
        Test Case1: babel-core
        """
        package_details = npm_analyser('babel-core')

        self.assertEqual(package_details.package_name, 'babel-core')
        self.assertEqual(package_details.license, 'MIT')
        
if __name__ == '__main__':
    unittest.main()

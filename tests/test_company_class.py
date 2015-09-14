import unittest
import os
import sys

# This makes it easy to import the needed files
sys.path.insert(0, os.path.abspath('..'))

from src.company_class import Company


class TestCompany(unittest.TestCase):
    def setUp(self):
        self.company = Company()

    def tearDown(self):
        pass

    def test_properties(self):
        pass

    def get_all_companies(self):
        pass

    def get_a_company(self):
        pass


if __name__ == "__main__":
    unittest.main()


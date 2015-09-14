import unittest
import os
import sys

# This makes it easy to import the needed files
sys.path.insert(0, os.path.abspath('..'))

from src.recruiter_class import Recruiter


class TestRecruiter(unittest.TestCase):
    def setup(self):
        self.contact = Recruiter()

    def test_properties(self):
        pass

    def test_full_name(self):
        pass

    def test_in_db(self):
        pass

    def test_get_all_recruiters(self):
        pass

    def test_a_recruiter(self):
        pass

    def test_company(self):
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

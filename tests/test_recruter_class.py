import unittest
import os
import sys

# This makes it easy to import the needed files
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from src.recruiter_class import Recruiter


class TestRecruiter(unittest.TestCase):
    def setUp(self):
        self.contact = Recruiter()

    @unittest.skip("Not implemented")
    def test_properties(self):
        pass

    @unittest.skip("Not implemented")
    def test_full_name(self):
        pass

    @unittest.skip("Not implemented")
    def test_in_db(self):
        pass

    @unittest.skip("Not implemented")
    def test_get_all_recruiters(self):
        pass

    @unittest.skip("Not implemented")
    def test_a_recruiter(self):
        pass

    @unittest.skip("Not implemented")
    def test_company(self):
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

import unittest
import os
import sys

# This makes it easy to import the needed files
sys.path.insert(0, os.path.abspath('..'))

from src.job_posting_class import JobPosting


class TestJobPosting(unittest.TestCase):
    def setUp(self):
        self.job_posting = JobPosting()

    def tearDown(self):
        pass

    def test_properties(self):
        pass

    def test_get_all_job_postings(self):
        pass

    def test_get_a_job_posting(self):
        pass


if __name__ == "__main__":
    unittest.main()

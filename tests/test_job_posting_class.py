import unittest
import os
import sys

# This makes it easy to import the needed files
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from src.job_posting_class import JobPosting


class TestJobPosting(unittest.TestCase):
    def setUp(self):
        self.info = {
            "uid": 1,
            "link": "www.test.com",
            "date_applied": "TIME NOW",
            "description": "Job posting Description",
            "interviewed": "Nope",
            "company_uid": 1,
            "recruiter_uid": 1,
            "contact_uid": 1
        }
        self.job_posting = JobPosting(
            self.info["uid"],
            self.info["link"],
            self.info["date_applied"],
            self.info["description"],
            self.info["interviewed"],
            self.info["company_uid"],
            self.info["recruiter_uid"],
            self.info["contact_uid"]
        )

    def tearDown(self):
        pass

    def test_properties(self):
        self.assertEqual(self.job_posting.uid, self.info["uid"])
        self.assertEqual(self.job_posting.link, self.info["link"])
        self.assertEqual(self.job_posting.date_applied, self.info["date_applied"])
        self.assertEqual(self.job_posting.description, self.info["description"])
        self.assertEqual(self.job_posting.interviewed, self.info["interviewed"])
        self.assertEqual(self.job_posting.company_uid, self.info["company_uid"])
        self.assertEqual(self.job_posting.recruiter_uid, self.info["recruiter_uid"])
        self.assertEqual(self.job_posting.contact_uid, self.info["contact_uid"])

    @unittest.skip("Not implemented")
    def test_get_all_job_postings(self):
        pass

    @unittest.skip("Not implemented")
    def test_get_a_job_posting(self):
        pass


if __name__ == "__main__":
    unittest.main()

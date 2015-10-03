import unittest
import os
import sys

# This makes it easy to import the needed files
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from src.job_posting_class import JobPosting
from src.sql_class import SQL


class TestJobPosting(unittest.TestCase):
    def setUp(self):
        self.info = {
            "uid": "",
            "link": "www.test.com",
            "date_applied": "2015-09-17",
            "description": "Job posting Description",
            "interviewed": "yes",
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

        self.new_description = "Testing!!!"
        self.total_of_job_postings = 1

        # Setting up the DB
        db = SQL()
        db.create_db()
        db.add_test_data_to_db()

    def test_properties(self):
        self.assertEqual(self.job_posting.uid, self.info["uid"])
        self.assertEqual(self.job_posting.link, self.info["link"])
        self.assertEqual(self.job_posting.date_applied, self.info["date_applied"])
        self.assertEqual(self.job_posting.description, self.info["description"])
        self.assertEqual(self.job_posting.interviewed, self.info["interviewed"])
        self.assertEqual(self.job_posting.company_uid, self.info["company_uid"])
        self.assertEqual(self.job_posting.recruiter_uid, self.info["recruiter_uid"])
        self.assertEqual(self.job_posting.contact_uid, self.info["contact_uid"])

    def test_get_all_job_postings(self):
        self.assertEqual(1, len(self.job_posting.get_all_job_postings()))

    def test_get_a_job_posting(self):
        data = self.job_posting.get_a_job_posting(1)[0]
        self.assertEqual("www.link.com", data.link)

    def test_add_job_posting_to_db(self):
        self.job_posting.add_job_posting_to_db()
        self.assertTrue(self.job_posting.uid)

    def test_update_job_posting_in_db(self):
        test_class = self.job_posting.get_a_job_posting(1)[0]
        test_class.description = self.new_description
        test_class.update_job_posting_in_db()
        test_class = self.job_posting.get_a_job_posting(1)[0]
        self.assertEqual(test_class.description, self.new_description)

    def test_delete_job_posting_in_db(self):
        test_class = self.job_posting.get_a_job_posting(1)[0]
        test_class.delete_job_posting_in_db()
        list_of_job_postings = self.job_posting.get_all_job_postings()
        self.assertEqual(len(list_of_job_postings), self.total_of_job_postings - 1)

if __name__ == "__main__":
    unittest.main()

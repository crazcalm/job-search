import unittest
import os
import sys

# This makes it easy to import the needed files
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from src.recruiter_class import Recruiter
from src.sql_class import SQL


class TestRecruiter(unittest.TestCase):
    def setUp(self):
        self.info = {
            "uid": "",
            "first_name": "Marcus",
            "last_name": "Willock",
            "email": "crazcalm@gmail.com",
            "phone": "111-222-3333",
            "description": "Nothing interesting",
            "company_uid": 1,
            "job_posting_uid": 1
        }
        self.recruiter = Recruiter(
            self.info["uid"],
            self.info["first_name"],
            self.info["last_name"],
            self.info["email"],
            self.info["phone"],
            self.info["description"],
            self.info["company_uid"],
            self.info["job_posting_uid"]
        )
        # Setting up the db
        db = SQL()
        db.create_db()
        db.add_test_data_to_db()

    def test_properties(self):
        self.assertEqual(self.recruiter.uid, self.info["uid"])
        self.assertEqual(self.recruiter.first_name, self.info["first_name"])
        self.assertEqual(self.recruiter.last_name, self.info["last_name"])
        self.assertEqual(self.recruiter.email, self.info["email"])
        self.assertEqual(self.recruiter.phone, self.info["phone"])
        self.assertEqual(self.recruiter.company_uid, self.info["company_uid"])
        self.assertEqual(self.recruiter.job_posting_uid, self.info["job_posting_uid"])

    def test_get_all_recruiters(self):
        self.assertEqual(7, len(self.recruiter.get_all_recruiters()))

    def test_a_recruiter(self):
        data = self.recruiter.get_a_recruiter(1)[0]
        self.assertEqual("Recruiter1", data.first_name)

    def test_add_recruiter_to_db(self):
        self.recruiter.add_recruiter_to_db()
        self.assertTrue(self.recruiter.uid)


if __name__ == "__main__":
    unittest.main()

import unittest
import os
import sys

# This makes it easy to import the needed files
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from src.company_class import Company
from src.contact_class import Contact
from src.job_posting_class import JobPosting
from src.recruiter_class import Recruiter
from src.sql_class import SQL
from src.cli_helper import show, class_factory, get_all_objects_in_db
from src.constants import COMPANY, COMPANIES, CONTACT, CONTACTS, RECRUITER, RECRUITERS, JOB_POSTING, JOB_POSTINGS


class CliHelper(unittest.TestCase):
    def setUp(self):
        self.class_list_plural = [CONTACTS, COMPANIES, RECRUITERS, JOB_POSTINGS]
        self.class_list = [CONTACT, COMPANY, RECRUITER, JOB_POSTING]
        self.classes = [Company, Contact, Recruiter, JobPosting]

        #Reset the database
        db = SQL()
        db.create_db()
        db.add_test_data_to_db()

    def test_show(self):
        for item in self.class_list_plural:
            self.assertIsNotNone(show(item))

    def test_class_factory(self):
        for item in self.class_list:
            self.assertIsNotNone(class_factory(item))

    def test_get_all_objects_in_db(self):
        for item in self.classes:
            print("class:", item)
            self.assertTrue(isinstance(get_all_objects_in_db(item()), list))



if __name__ == "__main__":
    unittest.main()

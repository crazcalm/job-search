import unittest
import os
import sys

# This makes it easy to import the needed files
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from src.company_class import Company
from src.sql_class import SQL


class TestCompany(unittest.TestCase):
    def setUp(self):
        self.info = {
            "uid": 1,
            "name": "Test Company",
            "address": "new york, NY",
            "website": "www.testing.com",
            "phone": "555-123-4567"}
        self.company = Company(
            self.info["uid"],
            self.info["name"],
            self.info["address"],
            self.info["website"],
            self.info["phone"]
        )

        #Reset the database
        db = SQL()
        db.create_db()
        db.add_test_data_to_db()

    def tearDown(self):
        pass

    def test_properties(self):
        self.assertEqual(self.company.uid, self.info["uid"])
        self.assertEqual(self.company.name, self.info["name"])
        self.assertEqual(self.company.address, self.info["address"])
        self.assertEqual(self.company.website, self.info["website"])
        self.assertEqual(self.company.phone, self.info["phone"])

    def test_get_all_companies(self):
        self.assertEqual(5, len(self.company.get_all_companies()))

    def test_get_a_company(self):
        data = self.company.get_a_company(1)[0]
        self.assertEqual("Google", data.name)


if __name__ == "__main__":
    unittest.main()


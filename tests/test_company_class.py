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
            "uid": "",
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
        self.new_uid = "6"
        self.new_name = "Testing!!!"

        #Reset the database
        db = SQL()
        db.create_db()
        db.add_test_data_to_db()

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

    def test_add_company_to_db(self):
        self.company.add_company_to_db()
        self.assertTrue(self.company.uid)

    @unittest.skip("I do not know how to test this without coupling this with another unit test")
    def test_update_company_in_db(self):
        pass

    @unittest.skip("I do not know how to test this without coupling this with another unit test")
    def test_delete_company_in_db(self):
        pass


if __name__ == "__main__":
    unittest.main()


import unittest
import os
import sys

# This makes it easy to import the needed files
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from src.company_class import Company


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

    def tearDown(self):
        pass

    def test_properties(self):
        self.assertEqual(self.company.uid, self.info["uid"])
        self.assertEqual(self.company.name, self.info["name"])
        self.assertEqual(self.company.address, self.info["address"])
        self.assertEqual(self.company.website, self.info["website"])
        self.assertEqual(self.company.phone, self.info["phone"])

    def get_all_companies(self):
        pass

    def get_a_company(self):
        pass


if __name__ == "__main__":
    unittest.main()


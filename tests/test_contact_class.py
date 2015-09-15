import unittest
import os
import sys

# This makes it easy to import the needed files
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from src.contact_class import Contact


class TestContact(unittest.TestCase):
    def setUp(self):
        self.info = {
            "uid": 1,
            "first_name": "Marcus",
            "last_name": "Willock",
            "email": "crazcalm@gmail.com",
            "phone": "xxx-xxx-xxxx",
            "description": "Creator",
            "company_uid": 1
        }

        self.contact = Contact(
            self.info["uid"],
            self.info["first_name"],
            self.info["last_name"],
            self.info["email"],
            self.info["phone"],
            self.info["description"],
            self.info["company_uid"]
        )

    def test_properties(self):
        self.assertTrue(self.contact)
        self.assertEqual(self.contact.uid, self.info["uid"])
        self.assertEqual(self.contact.first_name, self.info["first_name"])
        self.assertEqual(self.contact.last_name, self.info["last_name"])
        self.assertEqual(self.contact.email, self.info["email"])
        self.assertEqual(self.contact.phone, self.info["phone"])
        self.assertEqual(self.contact.description, self.info["description"])
        self.assertEqual(self.contact.company_uid, self.info["company_uid"])

    def test_full_name(self):
        pass

    @unittest.skip
    def test_in_db(self):
        pass

    @unittest.skip
    def test_get_all_contacts(self):
        pass

    @unittest.skip
    def test_a_contact(self):
        pass

    @unittest.skip
    def test_company(self):
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

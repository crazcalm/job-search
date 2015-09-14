import unittest
import os
import sys

# This makes it easy to import the needed files
sys.path.insert(0, os.path.abspath('..'))

from src.contact_class import Contact


class TestContact(unittest.TestCase):
    def setup(self):
        self.contact = Contact()

    def test_properties(self):
        pass

    def test_full_name(self):
        pass

    def test_in_db(self):
        pass

    def test_get_all_contacts(self):
        pass

    def test_a_contact(self):
        pass

    def test_company(self):
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()

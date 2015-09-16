import os
import sqlite3 as sqlite
try:
    from src.constants import TEST_DB
except ImportError:
    from constants import TEST_DB


class PracticalSQL:
    def __init__(self, db_path):
        # Note: the path might not exist yet...
        assert ";" not in db_path
        self.db_dir_path, self.db_name = os.path.split(db_path)
        self.db_path = os.path.abspath(db_path)
        self.con = sqlite.connect(db_path)

        # enable foreign keys
        self.con.execute("""PRAGMA foreign_keys = ON""")
        self.con.commit()

    def close(self):
        self.con.close()


class SQLModule:
    def __init__(self):
        self.db = None

    def init_db(self, db_path=TEST_DB):
        self.db = PracticalSQL(db_path)


class Person(SQLModule):
    def __init__(self, uid="", first_name="", last_name="", email="", phone="", description="",
                 company_uid=None):
        super().__init__()
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.description = description
        self.company_uid = company_uid

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

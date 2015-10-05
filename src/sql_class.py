import os
import subprocess

try:
    from src.base_classes import PracticalSQL
    from src.constants import TEST_DB, SQL_FILES, DB_TABLE_CREATION, DB_TEST_DATA
except ImportError:
    from base_classes import PracticalSQL
    from constants import TEST_DB, SQL_FILES, DB_TABLE_CREATION, DB_TEST_DATA


class SQL(PracticalSQL):
    singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = object.__new__(SQL)
        return cls.singleton

    def __init__(self, db_path=TEST_DB):
        super(SQL, self).__init__(db_path)

    def create_db(self):
        for table in DB_TABLE_CREATION:
            self.conn.execute(table.get("table"))
            self.conn.execute(table.get("columns"))
        self.conn.commit()

    def add_test_data_to_db(self):
        for lines in DB_TEST_DATA:
            for line in lines:
                self.conn.execute(line)
        self.conn.commit()


if __name__ == "__main__":
    test = SQL()
    test.create_db()
    test.add_test_data_to_db()

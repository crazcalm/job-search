from .base_classes import PracticalSQL
from .constants import REAL_DB, DB_TABLE_CREATION, DB_TEST_DATA


class SQL(PracticalSQL):
    """
    This class is dedicated to creating the database.
    """
    singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = object.__new__(SQL)
        return cls.singleton

    def __init__(self, db_path=REAL_DB):
        super(SQL, self).__init__(db_path)

    def create_db(self):
        """
        This method creates the tables and columns of the database.
        """
        for table in DB_TABLE_CREATION:
            self.conn.execute(table.get("table"))
            self.conn.execute(table.get("columns"))
        self.conn.commit()

    def add_test_data_to_db(self):
        """
        This method adds various test data to the database.
        """
        for lines in DB_TEST_DATA:
            for line in lines:
                self.conn.execute(line)
        self.conn.commit()


if __name__ == "__main__":
    pass

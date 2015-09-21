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
        self.conn = sqlite.connect(db_path)

        # enable foreign keys
        self.conn.execute("""PRAGMA foreign_keys = ON""")
        self.conn.commit()

    def close(self):
        self.conn.close()


class SQLModule:
    def __init__(self):
        self.db = None

    def init_db(self, db_path=TEST_DB):
        self.db = PracticalSQL(db_path)

    def update_row_in_db(self, table_name, columns, values):
        columns_string = "=?, ".join(columns) + "=? "
        query = """
        UPDATE {}
        SET {}
        WHERE id=?
        """.format(table_name, columns_string)

        self.db.conn.execute(query, values)
        self.db.conn.commit()

    def insert_row_into_db(self, table_name, columns, values):
        columns_string = "(" + ", ".join(columns) + ")"
        value_placeholder = "(" + "?, " * (len(columns) - 1) + "?)"
        query = """
        INSERT INTO {} {}
        VALUES {}
        """.format(table_name, columns_string, value_placeholder)

        self.db.conn.execute(query, values)
        self.db.conn.commit()

    def delete_row_in_db(self, table_name, uid):
        query = """
        DELETE FROM {}
        WHERE id=?
        """.format(table_name)

        self.db.conn.execute(query, uid)
        self.db.conn.commit()

    def get_id_of_last_row(self, table_name):
        query = """
        SELECT id
        FROM {}
        ORDER BY id
        DESC
        LIMIT 1
        """.format(table_name)

        items = self.db.conn.execute(query)

        # list of tuples
        uids = [uid for uid in items]

        # need to return the first item of the first tuple in the list
        return uids[0][0]

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


if __name__ == "__main__":
    test = SQLModule()
    table_name = "table_name"
    columns = ("id", "first_name", "last_name", "company")
    values = (1, "Marcus", "Willock", 1)
    #test.insert_row_into_db(table_name, columns, values)

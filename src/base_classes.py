from .constants import REAL_DB, TEST_DB

import os
import sqlite3 as sqlite


class PracticalSQL(object):
    """
    This class connects to the database and ensures that foreign keys
    for sqlite3 is turned on.
    """
    def __init__(self, db_path):
        """
        Initialization of the class.

        :param db_path: str - path to the database
        """
        # Note: the path might not exist yet...
        assert ";" not in db_path

        self.db_dir_path, self.db_name = os.path.split(db_path)
        self.db_path = os.path.abspath(db_path)
        self.conn = sqlite.connect(db_path)

        # enable foreign keys
        self.conn.execute("""PRAGMA foreign_keys = ON""")
        self.conn.commit()

    def close(self):
        """
        This method closes the db connection.
        """
        self.conn.close()


class SQLModule(object):
    """
    The class is used to be the connection bridge between the classes
    used in the application and the database.
    """
    def __init__(self):
        """
        Straight forward class initialization

        :return: None
        """
        self.db = None

    def _init_db(self, db_path=REAL_DB):
        """
        Initialized the database.

        :param db_path: str - Path to database
        :return: None
        """
        self.db = PracticalSQL(db_path)

    def init_db(self, testing=False):
        """
        Initializes the database. If testing is False, then a connection to
        the app database will be initialized. If not, a testing database will
        be initialized.

        :param testing: Boolean
        :return: None
        """
        if not self.db:
            if testing:
                self._init_db(TEST_DB)
            else:
                self._init_db(REAL_DB)

    def _update_row_in_db(self, table_name, columns, values):
        """
        This method provides a template for updating objects in the database.

        :param table_name: str
        :param columns: tuple
        :param values: tuple or list
        :return: None
        """
        columns_string = "=?, ".join(columns) + "=? "
        query = """
        UPDATE {}
        SET {}
        WHERE id=?
        """.format(table_name, columns_string)

        self.db.conn.execute(query, values)
        self.db.conn.commit()

    def _insert_row_into_db(self, table_name, columns, values):
        """
        This method provides a template for inserting objects into the database.

        :param table_name: str
        :param columns: tuple
        :param values: turple or list
        :return: None
        """
        columns_string = "(" + ", ".join(columns) + ")"
        value_placeholder = "(" + "?, " * (len(columns) - 1) + "?)"
        query = """
        INSERT INTO {} {}
        VALUES {}
        """.format(table_name, columns_string, value_placeholder)

        self.db.conn.execute(query, values)
        self.db.conn.commit()

    def _delete_row_in_db(self, table_name, uid):
        """
        This method provides a template for deleting objects in the database.

        :param table_name: str
        :param uid: tuple
        :return: None
        """
        query = """
        DELETE FROM {}
        WHERE id=?
        """.format(table_name)

        self.db.conn.execute(query, uid)
        self.db.conn.commit()

    def _get_id_of_last_row(self, table_name):
        """
        Retrieves the id of the last object in that database

        :param table_name: str
        """

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
    """
    This class is used as a perent class to Contact and Recruiter class. As a
    parent class, it contains the common functionality between the two classes.
    """
    def __init__(self, uid="", first_name="", last_name="", email="", phone="", description="",
                 company_uid=None, testing=False):
        """
        Initialization of the class.

        :param uid: int or empty str - db unique idetification number
        :param first_name: str
        :param last_name: str
        :param email: str
        :param phone: str
        :param description: str
        :param company_uid: str
        :param testing: boolean
        """
        super(Person, self).__init__()
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.description = description
        self.company_uid = company_uid
        self._testing = testing

    @property
    def company(self):
        if self.company_uid:
            from .company_class import Company
            self.init_db(self._testing)

            table_name = "company"
            query = """
            SELECT *
            FROM {}
            WHERE id=?
            """.format(table_name)

            results = self.db.conn.execute(query, (self.company_uid,))
            return [Company(*item) for item in results][0].name
        else:
            return self.company_uid

    @property
    def full_name(self):
        """
        Returns the full name of the person.
        """
        return "{} {}".format(self.first_name, self.last_name)


if __name__ == "__main__":
    pass

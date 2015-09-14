import os
import sqlite3 as sqlite


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

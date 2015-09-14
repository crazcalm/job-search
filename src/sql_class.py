import sqlite3 as sqlite
import os
import subprocess


class SQL:
    singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = object.__new__(SQL)
        return cls.singleton

    def __init__(self, db_path):
        # Note: the path might not exist yet...
        assert ";" not in db_path
        self.db_dir_path, self.db_name = os.path.split(db_path)
        self.db_path = os.path.abspath(db_path)
        self.con = sqlite.connect(db_path)

        # enable foreign keys
        self.con.execute("""PRAGMA foreign_keys = ON""")
        self.con.commit()

    def _add_data_to_db(self, file_path):
        assert os.path.isfile(file_path)

        subprocess.call("sqlite3 {} < {}".format(self.db_name, file_path), shell=True)

    def _add_data_from_dir(self, path_to_dir, data=False):
        assert os.path.isdir(path_to_dir)

        if data:
            sql_files = [file for file in os.listdir(path_to_dir) if file.endswith(".sql") and
                         "data" in file]
        else:
            sql_files = [file for file in os.listdir(path_to_dir) if file.endswith(".sql") and
                         "data" not in file]
        sql_files.sort()

        # Saving current dir and then changing to new dir
        old_cwd = os.getcwd()
        os.chdir(path_to_dir)

        for file in sql_files:
            print("current_file: ", file)
            self._add_data_to_db(file)

        # Returning to old directory
        os.chdir(old_cwd)

    def add_data_from_file(self, path):
        self._add_data_to_db(path)

    def add_data_from_dir(self, path, data=False):
        self._add_data_from_dir(path, data=data)

    def create_tables(self, path_to_dir):
        self._add_data_from_dir(path_to_dir)

    def close(self):
        self.con.close()


if __name__ == "__main__":
    test = SQL(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "SQL_files",
                                            "test.db")))
    sql_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "SQL_files"))
    play_data = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "SQL_files"))
    test.create_tables(sql_dir)
    test.add_data_from_dir(play_data, data=True)
import sqlite3 as sqlite
import os
import subprocess

from base_classes import PracticalSQL
from constants import TEST_DB, SQL_FILES


class SQL(PracticalSQL):
    singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls.singleton:
            cls.singleton = object.__new__(SQL)
        return cls.singleton

    def __init__(self, db_path):
        super().__init__(db_path)

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


if __name__ == "__main__":
    test = SQL(TEST_DB)
    test.create_tables(SQL_FILES)
    test.add_data_from_dir(SQL_FILES, data=True)

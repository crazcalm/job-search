import sqlite3 as sqlite
import os
import subprocess


class SQL:
    def __init__(self, db_path):
        self.db_name = self._db_name(db_path)
        self.con = sqlite.connect(db_path)

    def _db_name(self, db_path):
        if not db_path == ":memory:":
            assert ";" not in db_path

        return os.path.split(db_path)[1]

    def _add_data_to_db(self, file_path):
        assert os.path.isfile(file_path)

        subprocess.call("sqlite3 {} < {}".format(self.db_name, file_path), shell=True)

    def _add_data_from_dir(self, path_to_dir):
        assert os.path.isdir(path_to_dir)

        sql_files = [file for file in os.listdir(path_to_dir) if file.endswith(".sql")]
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

    def add_data_from_dir(self, path):
        self._add_data_from_dir(path)

    def create_tables(self, path_to_dir):
        self._add_data_from_dir(path_to_dir)

    def close(self):
        self.con.close()


if __name__ == "__main__":
    test = SQL(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "SQL_files",
                                            "test.db")))
    sql_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "SQL_files"))
    play_data = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "play_data"))
    test.create_tables(sql_dir)
    #test.add_data_from_dir(play_data)
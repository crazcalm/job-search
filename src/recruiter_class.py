try:
    from src.base_classes import Person
    from src.job_posting_class import JobPosting
except ImportError:
    from base_classes import Person
    from job_posting_class import JobPosting


# Note: a recruiter can have many job postings
class Recruiter(Person):
    _column = ["id", "first_name", "last_name", "email", "phone", "description", "companyId"]

    table_name = "recruiters"
    columns = tuple(_column[1:])
    columns_with_uid = tuple(_column)

    def __init__(self, uid="", first_name="", last_name="", email="", phone="", description="",
                 company_uid=None, testing=False):
        super(Recruiter, self).__init__(uid, first_name, last_name, email, phone, description, company_uid,
                                        testing=testing)

    @property
    def properties(self):
        return self.properties_with_uid[1:]

    @property
    def properties_with_uid(self):
        return "uid", "first_name", "last_name", "email", "phone", "description", "company_uid"

    @property
    def values(self):
        return self.first_name, self.last_name, self.email, self.phone, self.description, self.company_uid

    @property
    def values_with_uid(self):
        return self.first_name, self.last_name, self.email, self.phone, self.description, self.company_uid, self.uid

    @property
    def job_postings(self):
        if not self.db:
            self.init_db()

        table_name = "job_posting"
        query = """
        SELECT *
        FROM {}
        WHERE recruiterId=?
        """.format(table_name)

        results = self.db.conn.execute(query, (self.uid,))
        return [JobPosting(*item) for item in results]

    def get_all_recruiters(self):
        self.init_db(self._testing)

        query = "SELECT {} FROM {} ORDER BY id;".format(", ".join(Recruiter.columns_with_uid), Recruiter.table_name)

        data = self.db.conn.execute(query)

        return [Recruiter(*item) for item in data]

    def get_a_recruiter(self, uid):
        self.init_db(self._testing)

        query = "SELECT {} FROM {} WHERE (id=?) ORDER BY id;".format(
            ", ".join(Recruiter.columns_with_uid), Recruiter.table_name)

        data = self.db.conn.execute(query, (uid,))

        return [Recruiter(*item) for item in data]

    def get_job_postings(self):
        self.init_db(self._testing)

        # Add logic later
        pass

    def add_recruiter_to_db(self):
        self.init_db(self._testing)

        # make sure object is not in the db
        assert self.uid == ""

        self._insert_row_into_db(Recruiter.table_name, Recruiter.columns, self.values)

        # update the uid for current object
        self.uid = self._get_id_of_last_row(Recruiter.table_name)

    def update_recruiter_in_db(self):
        self.init_db(self._testing)

        # make sure that the object is in the db
        assert not self.uid == ""

        self._update_row_in_db(Recruiter.table_name, Recruiter.columns, self.values_with_uid)

    def delete_recruiter_in_db(self):
        self.init_db(self._testing)

        # make sure that the object is in the db
        assert not self.uid == ""

        self._delete_row_in_db(Recruiter.table_name, (self.uid,))

    def __str__(self):
        return """
        first name: {}
        last_name: {}
        email: {}
        phone: {}
        description: {}
        company_uid: {}
        number of job posting: {}""".format(
            self.first_name, self.last_name, self.email, self.phone, self.description,
            self.company_uid, len(self.job_postings))

if __name__ == "__main__":
    pass

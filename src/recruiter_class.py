try:
    from src.base_classes import Person
except ImportError:
    from base_classes import Person


# Note: a recruiter can have many job postings
class Recruiter(Person):
    table_name = "recruiters"
    columns = ("first_name", "last_name", "email", "phone", "description", "companyId")
    columns_with_uid = ("id", "first_name", "last_name", "email", "phone", "description", "companyId")

    def __init__(self, uid="", first_name="", last_name="", email="", phone="", description="",
                 company_uid=None, job_posting_uid=None):
        super().__init__(uid, first_name, last_name, email, phone, description, company_uid)
        self.job_posting_uid = job_posting_uid

    @property
    def values(self):
        return self.first_name, self.last_name, self.email, self.phone, self.description, self.company_uid

    @property
    def values_with_uid(self):
        return self.first_name, self.last_name, self.email, self.phone, self.description, self.company_uid, self.uid

    def get_all_recruiters(self):
        if not self.db:
            self.init_db()

        query = "SELECT {} FROM {} ORDER BY id;".format(", ".join(Recruiter.columns_with_uid), Recruiter.table_name)

        data = self.db.conn.execute(query)

        return [Recruiter(*item) for item in data]

    def get_a_recruiter(self, uid):
        if not self.db:
            self.init_db()
        query = "SELECT {} FROM {} WHERE (id=?) ORDER BY id;".format(
            ", ".join(Recruiter.company_uid), Recruiter.table_name)

        data = self.db.conn.execute(query, (uid,))

        return [Recruiter(*item) for item in data]

    def get_job_postings(self):
        if not self.db:
            self.init_db()

        # Add logic later
        pass

    def add_recruiter_to_db(self):
        if not self.db:
            self.init_db()

        # make sure object is not in the db
        assert self.uid == ""

        self.insert_row_into_db(Recruiter.table_name, Recruiter.columns, self.values)

    def update_recruiter_in_db(self):
        if not self.db:
            self.init_db()

        # make sure that the object is in the db
        assert not self.uid == ""

        self.update_row_in_db(Recruiter.table_name, Recruiter.columns, self.values_with_uid)

    def delete_recruiter_in_db(self):
        if not self.db:
            self.init_db()

        # make sure that the object is in the db
        assert  not self.uid == ""

        self.delete_row_in_db(Recruiter.table_name, self.uid)

    def __str__(self):
        return """
        uid: {}
        first name: {}
        last_name: {}
        email: {}
        phone: {}
        description: {}
        company_uid: {}
        job posting uid: {}""".format(
            self.uid, self.first_name, self.last_name, self.email, self.phone, self.description,
            self.company_uid, self.job_posting_uid)

if __name__ == "__main__":
    test = Recruiter(first_name="Marcus")
    for item in test.get_all_recruiters():
        print(item)


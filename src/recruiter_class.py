from .base_classes import Person


# Note: a recruiter can have many job postings
class Recruiter(Person):
    """
    This class is dedicated to modeling a recruiter.

    class properties include:
    - table_name: str
    - cloumns: tuple - db column names
    - columns_with_uid: tuple - db column names (including id)
    """
    _column = ["id", "first_name", "last_name", "email", "phone", "description", "companyId"]

    table_name = "recruiters"
    columns = tuple(_column[1:])
    columns_with_uid = tuple(_column)

    def __init__(self, uid="", first_name="", last_name="", email="", phone="", description="",
                 company_uid=None, testing=False):
        """
        Initialization of class.

        :param uid: int or empty string
        :param first_name: str
        :param last_name: str
        :param email: str
        :param phone: str
        :param description: str
        :param company_uid: int
        :param testing: boolean
        """

        # Initialization of the parent class
        super(Recruiter, self).__init__(uid, first_name, last_name, email, phone, description, company_uid,
                                        testing=testing)

    @property
    def properties(self):
        """
        Return a tuple of class property names
        """
        return self.properties_with_uid[1:]

    @property
    def properties_with_uid(self):
        """
        Return a tuple a class property names (including uid)
        """
        return "uid", "first_name", "last_name", "email", "phone", "description", "company_uid"

    @property
    def values(self):
        """
        Returns a tuple of class property values. The order is
        (first_name, last_name, email, phone, description, company_uid)
        """
        return self.first_name, self.last_name, self.email, self.phone, self.description, self.company_uid

    @property
    def values_with_uid(self):
        """
        Returns a tuple of class property values (including uid). The order is
        (first_name, last_name, email, phone, description, company_uid, uid)
        """
        return self.first_name, self.last_name, self.email, self.phone, self.description, self.company_uid, self.uid

    @property
    def job_postings(self):
        from .job_posting_class import JobPosting
        """
        Returns a list of job postings associated with this Recruiter.
        """
        self.init_db(self._testing)

        table_name = "job_posting"
        query = """
        SELECT *
        FROM {}
        WHERE recruiterId=?
        """.format(table_name)

        results = self.db.conn.execute(query, (self.uid,))
        return [JobPosting(*item) for item in results]

    def get_all_recruiters(self):
        """
        Returns a list of all of the Recruiters in the database.
        """
        self.init_db(self._testing)

        query = "SELECT {} FROM {} ORDER BY id;".format(", ".join(Recruiter.columns_with_uid), Recruiter.table_name)

        data = self.db.conn.execute(query)

        return [Recruiter(*item) for item in data]

    def get_a_recruiter(self, uid):
        """
        Returns a single Recruiter from the database

        :param uid: int
        """
        self.init_db(self._testing)

        query = "SELECT {} FROM {} WHERE (id=?) ORDER BY id;".format(
            ", ".join(Recruiter.columns_with_uid), Recruiter.table_name)

        data = self.db.conn.execute(query, (uid,))

        return [Recruiter(*item) for item in data]

    def add_recruiter_to_db(self):
        """
        This method adds this Recruiter instance to the database.
        """
        self.init_db(self._testing)

        # make sure object is not in the db
        assert self.uid == ""

        self._insert_row_into_db(Recruiter.table_name, Recruiter.columns, self.values)

        # update the uid for current object
        self.uid = self._get_id_of_last_row(Recruiter.table_name)

    def update_recruiter_in_db(self):
        """
        This method updates this Recruiter instance in the database.
        """
        self.init_db(self._testing)

        # make sure that the object is in the db
        assert not self.uid == ""

        self._update_row_in_db(Recruiter.table_name, Recruiter.columns, self.values_with_uid)

    def delete_recruiter_in_db(self):
        """
        This method deletes this Recruiter instance from the database.
        """
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

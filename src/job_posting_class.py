from .base_classes import SQLModule

from datetime import datetime


class JobPosting(SQLModule):
    """
    This class is dedicated to modeling a job posting.

    Class properties include:
    - table_name: str
    - columns: tuple - db column names
    - columns_with_uid: tuple - db column names (including id)
    """
    _columns = ["id", "link", "date_applied", "description", "interviewed", "companyId", "recruiterId",
                "contactId"]

    table_name = "job_posting"
    columns = tuple(_columns[1:])
    columns_with_uid = tuple(_columns)

    def __init__(self, uid="", link="", date_applied="", description="", interviewed="no",
                 company_uid=None, recruiter_uid=None, contact_uid=None, testing=False):
        """
        Initialization of class.

        :param uid: int or empty string
        :param link: str
        :param date_applied: str - Must be in the form of "yyyy-mm-dd"
        :param description: str
        :param interviewed: str - The only acceptable values are "yes" or "no"
        :param company_uid: int
        :param recruiter_uid: int
        :param contact_uid: int
        :param testing: boolean
        """

        # Initializing the parent class
        super(JobPosting, self).__init__()

        self.uid = uid
        self.link = link
        self._date_applied = None
        self.date_applied = date_applied
        self.description = description
        self._interviewed = "no"
        self.interviewed = interviewed
        self.company_uid = company_uid
        self.recruiter_uid = recruiter_uid
        self.contact_uid = contact_uid
        self._testing = testing

    @property
    def interviewed(self):
        """
        Returns a string of 'yes' or 'no'.
        """
        return self._interviewed

    @interviewed.setter
    def interviewed(self, value):
        """
        This setter ensure that this property will always have a valid
        value.

        Valid values are 'yes' and 'no'.
        """
        assert value.lower() in ("yes","no")
        self._interviewed = value

    @property
    def date_applied(self):
        """
        Returns a string that represents the data applied, which is of the
        form 'yyyy-mm-dd'.
        """
        return self._date_applied

    @date_applied.setter
    def date_applied(self, value):
        """
        This setter tries to ensure that this property will always have a
        valid value.

        Vaid values are stings of the form 'yyyy-mm-dd'
        """
        if value:
            assert 3 == len(value.split("-"))
            year, month, day = [int(item) for item in value.split("-")]
            date = datetime(year, month, day)
        else:
            date = datetime.now()
        self._date_applied = str(date).split(" ")[0]


    @property
    def properties(self):
        """
        Returns a tuple of class property names.
        """
        return self.properties_with_uid[1:]

    @property
    def properties_with_uid(self):
        """
        Returns a tuple of a class property names (including uid).
        """
        return ("uid", "link", "date_applied", "description", "interviewed", "company_uid", "recruiter_uid",
                        "contact_uid")

    @property
    def values(self):
        """
        Returns a tuple of class property values. The order is
        (link, date_applied, description, interviewed, company_uid,
         recruiter_uid, contact_uid)
        """
        return (self.link, self.date_applied, self.description, self.interviewed, self.company_uid,
                self.recruiter_uid, self.contact_uid)

    @property
    def values_with_uid(self):
        """
        Returns a tuple of class property values (including uid). The order is
        (link, date_applied, description, interviewed, company_uid,
         recruiter_uid, contact_uid, uid)
        """
        return (self.link, self.date_applied, self.description, self.interviewed, self.company_uid,
                self.recruiter_uid, self.contact_uid, self.uid)

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
            return [Company(*item) for item in results]
        else:
            return self.company_uid

    @property
    def contact(self):
        if self.contact_uid:
            from .contact_class import Contact
            self.init_db(self._testing)

            table_name = "contacts"
            query = """
            SELECT *
            FROM {}
            WHERE id=?
            """.format(table_name)

            results = self.db.conn.execute(query, (self.contact_uid,))
            return [Contact(*item) for item in results]
        else:
            return self.contact_uid

    @property
    def recruiter(self):
        if self.recruiter_uid:
            from .recruiter_class import Recruiter
            self.init_db(self._testing)

            table_name = "recruiters"
            query = """
            SELECT *
            FROM {}
            WHERE id=?
            """.format(table_name)

            results = self.db.conn.execute(query, (self.recruiter_uid,))
            return [Recruiter(*item) for item in results]
        else:
            return self.recruiter_uid

    def get_all_job_postings(self):
        """
        This method returns all of the job posting in the database.
        """
        self.init_db(self._testing)

        query = "SELECT {} FROM {} ORDER BY id;".format(", ".join(JobPosting.columns_with_uid), JobPosting.table_name)
        data = self.db.conn.execute(query)

        return [JobPosting(*item) for item in data]

    def get_a_job_posting(self, uid):
        """
        This method returns a single job posting from the database.
        """
        self.init_db(self._testing)

        query = "SELECT {} FROM {} WHERE (id=?) ORDER BY id;".format(", ".join(JobPosting.columns_with_uid), JobPosting.table_name)
        data = self.db.conn.execute(query, (uid,))

        return [JobPosting(*item) for item in data]

    def add_job_posting_to_db(self):
        """
        This method adds this job posting instance to the database.
        """
        self.init_db(self._testing)

        # make sure object is not in db
        assert self.uid == ""

        self._insert_row_into_db(JobPosting.table_name, JobPosting.columns, self.values)

        # need to update the uid on this object
        self.uid = self._get_id_of_last_row(JobPosting.table_name)

    def update_job_posting_in_db(self):
        """
        This method updates this job posting instance in the database.
        """
        self.init_db(self._testing)

        # make sure this object is in the db
        assert not self.uid == ""

        self._update_row_in_db(JobPosting.table_name, JobPosting.columns, self.values_with_uid)

    def delete_job_posting_in_db(self):
        """
        This method deletes this job posting instance in the database.
        """
        self.init_db(self._testing)

        # make sure this object is in the db
        assert not self.uid == ""

        self._delete_row_in_db(JobPosting.table_name, (self.uid,))

    def __str__(self):
        return """
        link: {}
        date applied: {}
        description: {}
        interviewed: {}
        company_uid: {}
        recruiter_uid: {}
        contact_uid: {}""".format(
            self.link, self.date_applied, self.description, self.interviewed,
            self.company_uid, self.recruiter_uid, self.contact_uid)


if __name__ == "__main__":
    pass


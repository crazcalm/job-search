try:
    from src.base_classes import SQLModule
except ImportError:
    from base_classes import SQLModule

from datetime import datetime


class JobPosting(SQLModule):
    _columns = ["id", "link", "date_applied", "description", "interviewed", "companyId", "recruiterId",
                        "contactId"]

    table_name = "job_posting"
    columns = tuple(_columns[1:])
    columns_with_uid = tuple(_columns)

    def __init__(self, uid="", link="", date_applied="", description="", interviewed="no",
                 company_uid=None, recruiter_uid=None, contact_uid=None):
        super().__init__()
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

    @property
    def interviewed(self):
        return self._interviewed

    @interviewed.setter
    def interviewed(self, value):
        assert value.lower() in ("yes","no")
        self._interviewed = value

    @property
    def date_applied(self):
        return self._date_applied

    # Once I now the db format for date, I can format it properly
    # Should I use regex to validate the string?
    @date_applied.setter
    def date_applied(self, value):
        if value:
            year, month, day = [int(item) for item in value.split("-")]
            date = datetime(year, month, day)
        else:
            date = datetime.now()
        self._date_applied = str(date).split(" ")[0]


    @property
    def properties(self):
        return self.properties_with_uid[1:]

    @property
    def properties_with_uid(self):
        return ("uid", "link", "date_applied", "description", "interviewed", "company_uid", "recruiter_uid",
                        "contact_uid")

    @property
    def values(self):
        return (self.link, self.date_applied, self.description, self.interviewed, self.company_uid,
                self.recruiter_uid, self.contact_uid)

    @property
    def values_with_uid(self):
        return (self.link, self.date_applied, self.description, self.interviewed, self.company_uid,
                self.recruiter_uid, self.contact_uid, self.uid)

    def get_all_job_postings(self):
        if not self.db:
            self.init_db()
        query = "SELECT {} FROM {} ORDER BY id;".format(", ".join(JobPosting.columns_with_uid), JobPosting.table_name)
        data = self.db.conn.execute(query)

        return [JobPosting(*item) for item in data]

    def get_a_job_posting(self, uid):
        if not self.db:
            self.init_db()
        query = "SELECT {} FROM {} WHERE (id=?) ORDER BY id;".format(", ".join(JobPosting.columns_with_uid), JobPosting.table_name)
        data = self.db.conn.execute(query, (uid,))

        return [JobPosting(*item) for item in data]

    def add_job_posting_to_db(self):
        if not self.db:
            self.init_db()

        # make sure object is not in db
        assert self.uid == ""

        self._insert_row_into_db(JobPosting.table_name, JobPosting.columns, self.values)

        # need to update the uid on this object
        self.uid = self._get_id_of_last_row(JobPosting.table_name)

    def update_job_posting_in_db(self):
        if not self.db:
            self.init_db()

        # make sure this object is in the db
        assert not self.uid == ""

        self._update_row_in_db(JobPosting.table_name, JobPosting.columns, self.values_with_uid)

    def delete_job_posting_in_db(self):
        if not self.db:
            self.init_db()

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
    test = JobPosting(link="Testing", date_applied="2015-01-19")
    test.interviewed = "yes"
    print(test)
    #test.add_job_posting_to_db()

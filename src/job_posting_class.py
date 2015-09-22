try:
    from src.base_classes import SQLModule
except ImportError:
    from base_classes import SQLModule


class JobPosting(SQLModule):

    table_name = "job_posting"
    columns = ("link", "date_applied", "description", "interviewed", "companyId", "recruiterId", "contactId")
    columns_with_uid = ("id", "link", "date_applied", "description", "interviewed", "companyId", "recruiterId",
                        "contactId")

    def __init__(self, uid="", link="", date_applied="", description="", interviewed="",
                 company_uid=None, recruiter_uid=None, contact_uid=None):
        super().__init__()
        self.uid = uid
        self.link = link
        self.date_applied = date_applied
        self.description = description
        self.interviewed = interviewed
        self.company_uid = company_uid
        self.recruiter_uid = recruiter_uid
        self.contact_uid = contact_uid

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

        self.insert_row_into_db(JobPosting.table_name, JobPosting.columns, self.values)

        # need to update the uid on this object
        self.uid = self.get_id_of_last_row(JobPosting.table_name)

    def update_job_posting_in_db(self):
        if not self.db:
            self.init_db()

        # make sure this object is in the db
        assert not self.uid == ""

        self.update_row_in_db(JobPosting.table_name, JobPosting.columns, self.values_with_uid)

    def delete_job_posting_in_db(self):
        if not self.db:
            self.init_db()

        # make sure this object is in the db
        assert not self.uid == ""

        self.delete_row_in_db(JobPosting.table_name, (self.uid,))

    def __str__(self):
        return """
        uid: {}
        link: {}
        date applied: {}
        description: {}
        interviewed: {}
        company_uid: {}
        recruiter_uid: {}
        contact_uid: {}""".format(
            self.uid, self.link, self.date_applied, self.description, self.interviewed,
            self.company_uid, self.recruiter_uid, self.contact_uid)


if __name__ == "__main__":
    test = JobPosting(link="Testing")
    print(test)
    test.add_job_posting_to_db()

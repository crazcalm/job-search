try:
    from src.base_classes import Person
except ImportError:
    from base_classes import Person


# Note: a recruiter can have many job postings
class Recruiter(Person):
    def __init__(self, uid="", first_name="", last_name="", email="", phone="", description="",
                 company_uid=None, job_posting_uid=None):
        super().__init__(uid, first_name, last_name, email, phone, description, company_uid)
        self.job_posting_uid = job_posting_uid

    def get_all_recruiters(self):
        if not self.db:
            self.init_db()

        query = """
        SELECT id, first_name, last_name, email, phone, description, companyId
        FROM recruiters ORDER BY id;
        """
        data = self.db.conn.execute(query)

        return [Recruiter(*item) for item in data]

    def get_a_recruiter(self, uid):
        if not self.db:
            self.init_db()
        query = """
        SELECT id, first_name, last_name, email, phone, description, companyId FROM recruiters
        WHERE (id=?) ORDER BY id;
        """
        data = self.db.conn.execute(query, (uid,))
        return [Recruiter(*item) for item in data]

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


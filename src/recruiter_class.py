try:
    from src.contact_class import Contact
except ImportError:
    from contact_class import Contact


# Note: a recruiter can have many job postings
class Recruiter(Contact):
    def __init__(self, uid="", first_name="", last_name="", email="", phone="", description="",
                 company_uid=None, job_posting_uid=None):
        super().__init__(uid, first_name, last_name, email, phone, description, company_uid)
        self.job_posting_uid = job_posting_uid

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
    print(test)

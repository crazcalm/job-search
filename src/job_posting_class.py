try:
    from src.base_classes import SQLModule
except ImportError:
    from base_classes import SQLModule


class JobPosting(SQLModule):
    def __init__(self, uid="", link="", date_applied="", description="", interviewed="",
                company_uid=None, recruiter_uid=None, contact_uid=None):
        super()
        self.uid = uid
        self.link = link
        self.date_applied = date_applied
        self.description = description
        self.interviewed = interviewed
        self.company_uid = company_uid
        self.recruiter_uid = recruiter_uid
        self.contact_uid = contact_uid

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

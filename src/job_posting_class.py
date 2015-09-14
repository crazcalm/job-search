from base_classes import SQLModule


class JobPosting(SQLModule):
    def __int__(self, uid="", link="", date_applied="", description="", interviewed="",
                company_uid="", recruiter_uid="", contact_uid=""):
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

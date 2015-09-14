class JobPosting:
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

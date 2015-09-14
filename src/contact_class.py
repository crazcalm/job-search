class Contact:
    def __init__(self, uid="", first_name="", last_name="", email="", phone="", description="",
                 company_id=None):
        self.id = uid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.description = description
        self.company_id = company_id

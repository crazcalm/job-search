try:
    from src.base_classes import SQLModule
except ImportError:
    from base_classes import SQLModule


class Contact(SQLModule):
    def __init__(self, uid="", first_name="", last_name="", email="", phone="", description="",
                 company_uid=None):
        super()
        self.uid = uid
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.description = description
        self.company_uid = company_uid

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return """
        uid: {}
        first name: {}
        last_name: {}
        email: {}
        phone: {}
        description: {}
        company_uid: {}""".format(
            self.uid, self.first_name, self.last_name, self.email, self.phone, self.description,
            self.company_uid)

if __name__ == "__main__":
    test = Contact(first_name="Marcus")
    print(test)

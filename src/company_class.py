from sql_class import SQL


class Company:
    def __init__(self, uid="", name="", address="", website="", phone=""):
        self.uid = uid
        self.name = name
        self.address = address
        self.website = website
        self.phone = phone

    def __str__(self):
        return """
        uid: {}
        name: {}
        address: {}
        website: {}
        phone: {}""".format(self.uid, self.name, self.address, self.website, self.phone)

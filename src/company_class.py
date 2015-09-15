try:
    from src.base_classes import SQLModule
except ImportError:
    from base_classes import SQLModule


class Company(SQLModule):
    def __init__(self, uid="", name="", address="", website="", phone=""):
        super()
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

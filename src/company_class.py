try:
    from src.base_classes import SQLModule
except ImportError:
    from base_classes import SQLModule


class Company(SQLModule):
    def __init__(self, uid="", name="", address="", website="", phone=""):
        super().__init__()
        self.uid = uid
        self.name = name
        self.address = address
        self.website = website
        self.phone = phone

    def get_all_companies(self):
        if not self.db:
            self.init_db()

        query = """
        SELECT id, name, address, website, phone FROM company ORDER BY id;
        """

        data = self.db.conn.execute(query)

        return [Company(*item) for item in data]

    def get_a_company(self, uid):
        assert isinstance(uid, int)
        if not self.db:
            self.init_db()

        query = """
        SELECT id, name, address, website, phone FROM company WHERE (id=?) ORDER BY id
        """

        data = self.db.conn.execute(query, (uid,))

        return [Company(*item) for item in data]

    def __str__(self):
        return """
        uid: {}
        name: {}
        address: {}
        website: {}
        phone: {}""".format(self.uid, self.name, self.address, self.website, self.phone)

if __name__ == "__main__":
    test = Company(name="Crazcalm")
    test.get_all_companies()
    print(test.get_a_company(1)[0])

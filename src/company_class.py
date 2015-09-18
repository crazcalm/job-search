try:
    from src.base_classes import SQLModule
except ImportError:
    from base_classes import SQLModule


class Company(SQLModule):
    table_name = "company"
    columns = ("name", "address", "website", "phone")
    columns_with_uid = ("id", "name", "address", "website", "phone")

    def __init__(self, uid="", name="", address="", website="", phone=""):
        super().__init__()
        self.uid = uid
        self.name = name
        self.address = address
        self.website = website
        self.phone = phone
        self.values = (self.name, self.address, self.website, self.phone)
        self.values_with_id = (self.name, self.address, self.website, self.phone, self.uid)

    def get_all_companies(self):
        if not self.db:
            self.init_db()

        query = "SELECT {} FROM company ORDER BY id;".format(", ".join(Company.columns_with_uid))

        data = self.db.conn.execute(query)

        return [Company(*item) for item in data]

    def get_a_company(self, uid):
        assert isinstance(uid, int)
        if not self.db:
            self.init_db()

        query = "SELECT {} FROM company WHERE (id=?) ORDER BY id;".format(", ".join(Company.columns_with_uid))

        data = self.db.conn.execute(query, (uid,))

        return [Company(*item) for item in data]

    def add_company_to_db(self):
        if not self.db:
            self.init_db()

        # Make sure that the Company does not already exist
        assert self.uid == ""

        self.insert_row_into_db(Company.table_name, Company.columns, self.values)

    def update_company_in_db(self):
        if not self.db:
            self.init_db()

        # make sure tht the Company does exist in the
        assert not self.uid == ""

        self.update_row_in_db(Company.table_name, Company.columns, self.values_with_id)

    def delete_a_company(self):
        if not self.db:
            self.init_db()

        # Make sure that the Company exists
        assert not self.uid == ""

        self.delete_row_in_db(Company.table_name, self.uid)

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

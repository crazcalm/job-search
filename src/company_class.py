try:
    from src.base_classes import SQLModule
    from src.constants import REAL_DB, TEST_DB
except ImportError:
    from base_classes import SQLModule
    from constants import REAL_DB, TEST_DB


class Company(SQLModule):
    _columns = ["id", "name", "address", "website", "phone"]
    table_name = "company"
    columns = tuple(_columns[1:])
    columns_with_uid = tuple(_columns)

    def __init__(self, uid="", name="", address="", website="", phone="", testing=False):
        super(Company, self).__init__()
        self.uid = uid
        self.name = name
        self.address = address
        self.website = website
        self.phone = phone
        self._testing = testing

    @property
    def properties(self):
        return self.properties_with_uid[1:]

    @property
    def properties_with_uid(self):
        return "uid", "name", "address", "website", "phone"

    @property
    def values(self):
        return self.name, self.address, self.website, self.phone

    @property
    def values_with_id(self):
        return self.name, self.address, self.website, self.phone, self.uid

    def get_all_companies(self):
        self.init_db(self._testing)

        query = "SELECT {} FROM {} ORDER BY id;".format(", ".join(Company.columns_with_uid), Company.table_name)

        data = self.db.conn.execute(query)

        return [Company(*item) for item in data]

    def get_a_company(self, uid):
        assert isinstance(uid, int)
        self.init_db(self._testing)

        query = "SELECT {} FROM {} WHERE (id=?) ORDER BY id;".format(
            ", ".join(Company.columns_with_uid), Company.table_name)

        data = self.db.conn.execute(query, (uid,))

        return [Company(*item) for item in data]

    def add_company_to_db(self):
        self.init_db(self._testing)

        # Make sure that the Company does not already exist
        assert self.uid == ""

        self._insert_row_into_db(Company.table_name, Company.columns, self.values)

        # updating the uid for the current object
        self.uid = self._get_id_of_last_row(Company.table_name)

    def update_company_in_db(self):
        self.init_db(self._testing)

        # make sure tht the Company does exist in the
        assert not self.uid == ""

        self._update_row_in_db(Company.table_name, Company.columns, self.values_with_id)

    def delete_company_in_db(self):
        self.init_db(self._testing)

        # Make sure that the Company exists
        assert not self.uid == ""

        self._delete_row_in_db(Company.table_name, (self.uid,))

    def __str__(self):
        return """
        name: {}
        address: {}
        website: {}
        phone: {}""".format(self.name, self.address, self.website, self.phone)

if __name__ == "__main__":
    test = Company(name="DavidInc")
    print(test.columns)

try:
    from src.base_classes import SQLModule, Person
except ImportError:
    from base_classes import SQLModule, Person


class Contact(Person):
    _columns = ["id", "first_name", "last_name", "email", "phone", "description", "companyId"]

    table_name = "contacts"
    columns = tuple(_columns[1:])
    columns_with_uid = tuple(_columns)

    def __init__(self, uid="", first_name="", last_name="", email="", phone="", description="",
                 company_uid=None):
        super().__init__(uid, first_name, last_name, email, phone, description, company_uid)

    @property
    def properties(self):
        return self.properties_with_uid[1:]

    @property
    def properties_with_uid(self):
        return "uid", "first_name", "last_name", "email", "phone", "description", "company_uid"

    @property
    def values(self):
        return self.first_name, self.last_name, self.email, self.phone, self.description, self.company_uid

    @property
    def values_with_uid(self):
        return self.first_name, self.last_name, self.email, self.phone, self.description, self.company_uid, self.uid

    def get_all_contacts(self):
        if not self.db:
            self.init_db()

        query = "SELECT {} FROM {} ORDER BY id;".format(", ".join(Contact.columns_with_uid), Contact.table_name)

        data = self.db.conn.execute(query)

        return [Contact(*item) for item in data]

    def get_a_contact(self, uid):
        if not self.db:
            self.init_db()

        query = "SELECT {} FROM {} WHERE (id=?) ORDER BY id;".format(
            ", ".join(Contact.columns_with_uid), Contact.table_name)

        data = self.db.conn.execute(query, (uid,))

        return [Contact(*item) for item in data]

    def add_contact_to_db(self):
        if not self.db:
            self.init_db()

        # make sure that the object is not in the db
        assert self.uid == ""

        self._insert_row_into_db(Contact.table_name, Contact.columns, self.values)

        # update this objects uid
        self.uid = self._get_id_of_last_row(Contact.table_name)

    def update_contact_in_db(self):
        if not self.db:
            self.init_db()

        # making sure that the object is in the db
        assert not self.uid == ""

        self._update_row_in_db(Contact.table_name, Contact.columns, self.values_with_uid)

    def delete_contact_in_db(self):
        if not self.db:
            self.init_db()

        # making sure that the object is in the db
        assert not self.uid == ""

        self._delete_row_in_db(Contact.table_name, (self.uid,))

    def __str__(self):
        return """
        first name: {}
        last_name: {}
        email: {}
        phone: {}
        description: {}
        company_uid: {}""".format(
            self.first_name, self.last_name, self.email, self.phone, self.description,
            self.company_uid)

if __name__ == "__main__":
    test = Contact(first_name="Marcus")
    print(test)
    test.get_all_contacts()
    print(test.get_a_contact(1)[0])

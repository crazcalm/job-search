try:
    from src.base_classes import SQLModule, Person
except ImportError:
    from base_classes import SQLModule, Person


class Contact(Person):
    def __init__(self, uid="", first_name="", last_name="", email="", phone="", description="",
                 company_uid=None):
        super().__init__(uid, first_name, last_name, email, phone, description, company_uid)

    def get_all_contacts(self):
        if not self.db:
            self.init_db()

        query = """
        SELECT id, first_name, last_name, email, phone, description, companyId
        FROM contacts ORDER BY id;
        """

        data = self.db.con.execute(query)

        return [Contact(*item) for item in data]

    def get_a_contact(self, uid):
        if not self.db:
            self.init_db()

        query = """
        SELECT id, first_name, last_name, email, phone, description, companyId
        FROM contacts WHERE (id=?) ORDER BY id;
        """

        data = self.db.con.execute(query, (uid,))

        return [Contact(*item) for item in data]

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
    test.get_all_contacts()
    print(test.get_a_contact(1)[0])

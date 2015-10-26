from .base_classes import Person


class Contact(Person):
    """
    This class is dedicated to modeling a company contact.

    Class properties include:
    - table_name: str
    - columns: tuple - db column names
    - columns_with_uid: tuple - db column names (including uid)
    """
    _columns = ["id", "first_name", "last_name", "email", "phone", "description", "companyId"]

    table_name = "contacts"
    columns = tuple(_columns[1:])
    columns_with_uid = tuple(_columns)

    def __init__(self, uid="", first_name="", last_name="", email="", phone="", description="",
                 company_uid=None, testing=False):
        """
        Initialization of the class

        :param uid: int or empty str - db unique identifier
        :param first_name: str
        :param last_name: str
        :param email: str
        :param phone: str
        :param description: str
        :param company_uid: int
        :param testing: boolean
        """

        # Initialization of the parent class
        super(Contact, self).__init__(uid, first_name, last_name, email, phone, description, company_uid,
                                      testing=testing)

    @property
    def properties(self):
        """
        Returns a tuple of class property names
        """
        return self.properties_with_uid[1:]

    @property
    def properties_with_uid(self):
        """
        Returns a tuple of class property names (including uid)
        """
        return "uid", "first_name", "last_name", "email", "phone", "description", "company_uid"

    @property
    def values(self):
        """
        Returns a tuple of class property values. The order is
        (first_name, last_name, email, phone, description, company_uid)
        """
        return self.first_name, self.last_name, self.email, self.phone, self.description, self.company_uid

    @property
    def values_with_uid(self):
        """
        Returns a tuple of class property values (including uid). The order is
        (first_name, last_name, email, phone, description, company_uid, uid)
        """
        return self.first_name, self.last_name, self.email, self.phone, self.description, self.company_uid, self.uid

    def get_all_contacts(self):
        """
        This method returns all of the contacts in the database.
        """
        self.init_db(self._testing)

        query = "SELECT {} FROM {} ORDER BY id;".format(", ".join(Contact.columns_with_uid), Contact.table_name)

        data = self.db.conn.execute(query)

        return [Contact(*item) for item in data]

    def get_a_contact(self, uid):
        """
        This methods returns a single contact from the database.

        :param uid: int
        """
        self.init_db(self._testing)

        query = "SELECT {} FROM {} WHERE (id=?) ORDER BY id;".format(
            ", ".join(Contact.columns_with_uid), Contact.table_name)

        data = self.db.conn.execute(query, (uid,))

        return [Contact(*item) for item in data]

    def add_contact_to_db(self):
        """
        This method adds this Contact instance to the database.
        """
        self.init_db(self._testing)

        # make sure that the object is not in the db
        assert self.uid == ""

        self._insert_row_into_db(Contact.table_name, Contact.columns, self.values)

        # update this objects uid
        self.uid = self._get_id_of_last_row(Contact.table_name)

    def update_contact_in_db(self):
        """
        This method updates this Contact instance in the database.
        """
        self.init_db(self._testing)

        # making sure that the object is in the db
        assert not self.uid == ""

        self._update_row_in_db(Contact.table_name, Contact.columns, self.values_with_uid)

    def delete_contact_in_db(self):
        """
        This method deletes this Contact instance in the database.
        """
        self.init_db(self._testing)

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
        company: {}""".format(
            self.first_name, self.last_name, self.email, self.phone, self.description,
            self.company)

if __name__ == "__main__":
    pass

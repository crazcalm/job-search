try:
    from src.company_class import Company
    from src.contact_class import Contact
    from src.recruiter_class import Recruiter
    from src.job_posting_class import JobPosting
    from src.constants import CONTACT, COMPANY, RECRUITER, JOB_POSTING
    from src.constants import CONTACTS, COMPANIES, RECRUITERS, JOB_POSTINGS
except ImportError:
    from company_class import Company
    from contact_class import Contact
    from recruiter_class import Recruiter
    from job_posting_class import JobPosting
    from constants import CONTACT, COMPANY, RECRUITER, JOB_POSTING
    from constants import CONTACTS, COMPANIES, RECRUITERS, JOB_POSTINGS

CLASS_MAPPING = {
    COMPANY: {
        "class": Company,
        "get_all": "get_all_companies",
        "add_to_db": "add_company_to_db",
        "update_in_db": "update_company_in_db"
    },
    CONTACT: {
        "class": Contact,
        "get_all": "get_all_contacts",
        "add_to_db": "add_contact_to_db",
        "update_in_db": "update_contact_in_db"
    },
    RECRUITER: {
        "class": Recruiter,
        "get_all": "get_all_recruiters",
        "add_to_db": "add_recruiter_to_db",
        "update_in_db": "update_recruiter_in_db"
    },
    JOB_POSTING: {
        "class": JobPosting,
        "get_all": "get_all_job_postings",
        "add_to_db": "add_job_posting_to_db",
        "update_in_db": "update_job_posting_in_db"
    }
}

CLASSES_PLURAL_MAPPING = {
    COMPANIES: CLASS_MAPPING.get(COMPANY),
    CONTACTS: CLASS_MAPPING.get(CONTACT),
    RECRUITERS: CLASS_MAPPING.get(RECRUITER),
    JOB_POSTINGS: CLASS_MAPPING.get(JOB_POSTING)
}


def _get_a_class_instance(class_name, uid):
    class_object = class_factory(class_name)
    wanted_class = None

    if class_name in CLASS_MAPPING:
        if class_name == COMPANY:
            wanted_class = class_object.get_a_company(uid)

        elif class_name == Contact:
            wanted_class = class_object.get_a_contact(uid)

        elif class_name == RECRUITER:
            wanted_class = class_object.get_a_recruiter(uid)

        else:
            wanted_class = class_object.get_a_job_posting(uid)
    return wanted_class


def _get_class_name_from_class_instance(class_object):
    return str(type(class_object)).split(".")[-1][:-2].lower()


def save_class_object(class_object):
    class_name = _get_class_name_from_class_instance(class_object)
    class_info = CLASS_MAPPING[class_name]

    if class_object.uid:
        method_name = class_info['update_in_db']
        getattr(class_object, method_name)()

    else:
        method_name = class_info['add_to_db']
        getattr(class_object, method_name)()


def show(class_type):
    """
    This function is used to get the list of all the objects in the database of a
    specific class.

    :param class_type: str - Lowercase string of the plural form of the class name
    :return: list of class instances or None
    """
    result = None
    if class_type in CLASSES_PLURAL_MAPPING:
        class_info = CLASSES_PLURAL_MAPPING.get(class_type)
        instance = class_info.get("class")()
        result = get_all_objects_in_db(instance)
    return result


def class_factory(class_name, mapping=CLASS_MAPPING):
    """
    This function takes a lowercase string version of the class name and returns
    an instance of that class.

    :param class_name: str - Lowercase string of the class name
    :param mapping: dict - maps the string the to class
    :return: class instance
    """
    return mapping.get(class_name).get("class")()


def get_all_objects_in_db(class_object):
    """
    This function takes an instance of the class and returns a list
    of objects from the database.

    :param class_object: class instance
    :return: list of class instances
    """
    # Parsing the type string to get the class name
    class_name = _get_class_name_from_class_instance(class_object)

    # getting the needed method name
    method_name = CLASS_MAPPING.get(class_name).get("get_all")

    return getattr(class_object, method_name)()


def _segregate_properties(properties):
    class_properties = [prop for prop in properties if "uid" not in prop.lower()]
    class_properties_references = [prop for prop in properties if prop not in class_properties]
    return class_properties, class_properties_references


# Need to add filtering on the properties so that
# x,y,z properties lead to a selection screen for those class objects
def update_class(class_object, properties):
    """
    This function controls the loop that updates the properties of a class.

    :param class_object: class instance
    :param properties: tuple of properties to update
    :return: None
    """
    print("Pressing enter will leave the value unchanged.\n")

    # list of properties with
    class_properties, class_properties_references = _segregate_properties(properties)

    print("class_properties:", class_properties)
    print("class_properties_references:", class_properties_references)

    for prop in properties:

        if prop in class_properties:
            value = getattr(class_object, prop)
            new_value = input("\nCurrent value of {}: {}\nEnter new value: ".format(prop, value))

            if new_value:
                setattr(class_object, prop, new_value)

        if prop in class_properties_references:
            class_name = prop.split("_")[0]

            # Check to see of that property has a valid value
            if getattr(class_object, prop):
                wanted_instance = _get_a_class_instance(class_name, getattr(class_object, prop))
                print("Current {}: \n{}".format(class_name, wanted_instance))
            else:
                wanted_instance = class_factory(class_name)
                print("Current {}: \n Is not assigned".format(class_name))

            user_input = input("If you want to change the associated {}, enter 'YES': ".format(class_name))

            if user_input.lower() in ("yes", "y"):
                # enter the selection process
                selected_class = selection_screen(get_all_objects_in_db(wanted_instance))

                if selected_class:
                    setattr(class_object, prop, selected_class.uid)
    print(class_object)
    save_class_object(class_object)


# Need to add the get_other_classes_methods to the classes that
# reference other classes. After that, I need to implement the verbose
# functionality, which will print the object in question and the linked objects
def print_to_screen(list_of_classes, verbose=False):
    """
    This function prints the objects to the screen.

    :param list_of_classes: list of class instances
    :param verbose: Boolean
    :return: None
    """
    for index, item in enumerate(list_of_classes):
        print("{}: {}\n\n".format(index + 1, item))


def selection_screen(list_of_classes):
    """
    This function controls the selection screen used allow the
    user to select a class instance from a list of class instances.

    :param list_of_classes: list of class objects
    :return: None
    """
    user_input = None
    while not user_input and user_input != 0:
        print_to_screen(list_of_classes)
        tempt = input("Enter the number of the class that you to select: ")

        try:
            user_input = int(tempt) - 1
        except ValueError:
            print("{} is not a valid input. Hit enter to continue.".format(tempt))
            input()

    return list_of_classes[user_input]

if __name__ == "__main__":
    test = Recruiter()
    update_class(test, test.properties)

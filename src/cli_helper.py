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
        "get_all": "get_all_companies"
    },
    CONTACT: {
        "class": Contact,
        "get_all": "get_all_contacts"
    },
    RECRUITER: {
        "class": Recruiter,
        "get_all": "get_all_recruiters"
    },
    JOB_POSTING: {
        "class": JobPosting,
        "get_all": "get_all_job_postings"
    }
}

CLASSES_PLURAL_MAPPING = {
    COMPANIES: CLASS_MAPPING.get(COMPANY),
    CONTACTS: CLASS_MAPPING.get(CONTACT),
    RECRUITERS: CLASS_MAPPING.get(RECRUITER),
    JOB_POSTINGS: CLASS_MAPPING.get(JOB_POSTING)
}


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
    class_name = str(type(class_object)).split(".")[-1][:-2].lower()

    # getting the needed method name
    method_name = CLASS_MAPPING.get(class_name).get("get_all")

    return getattr(class_object, method_name)()


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
    for prop in properties:
        value = getattr(class_object, prop)
        new_value = input("\nCurrent value of {}: {}\nEnter new value: ".format(prop, value))

        if new_value:
            setattr(class_object, prop, new_value)
    print(class_object)


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
    while not user_input:
        print_to_screen(list_of_classes)
        tempt = input("Enter the number of the class that you to select: ")

        try:
            user_input = int(tempt) - 1
        except ValueError:
            print("{} is not a valid input. Hit enter to continue.".format(tempt))
            input()

    return list_of_classes[user_input]

if __name__ == "__main__":
    pass

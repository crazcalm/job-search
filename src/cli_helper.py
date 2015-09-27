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
    result = None
    if class_type in CLASSES_PLURAL_MAPPING:
        class_info = CLASSES_PLURAL_MAPPING.get(class_type)
        instance = class_info.get("class")()
        result = getattr(instance, class_info.get("get_all"))()
    return result


def class_factory(class_name, mapping=CLASS_MAPPING):
    return mapping.get(class_name).get("class")()


def get_all_objects_in_db(class_object):
    # Parsing the type string to get the class name
    class_name = str(type(class_object)).split(".")[-1][:-2].lower()

    # getting the needed method name
    method_name = CLASS_MAPPING.get(class_name).get("get_all")

    return getattr(class_object, method_name)()


def update_class(class_object, properties):
    print("Pressing enter will leave the value unchanged.\n")
    for prop in properties:
        value = getattr(class_object, prop)
        new_value = input("\nCurrent value: {}\nEnter new value: ".format(value))

        if new_value:
            setattr(class_object, prop, new_value)
    print(class_object)


def print_to_screen(list_of_classes, verbose=False):
    for index, item in enumerate(list_of_classes):
        print("{}: {}\n\n".format(index + 1, item))


def selection_screen(list_of_classes):
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
    #testing = class_factory("company")

    #list_of_objects = get_all_objects_in_db(testing)

    #print_to_screen(list_of_objects)
    #print(selection_screen(list_of_objects))

    test_class = Company()
    test = test_class.get_all_companies()
    print_to_screen(test)

    #testing = test_class.get_a_company(1)[0]
    #update_class(testing, Company.columns)

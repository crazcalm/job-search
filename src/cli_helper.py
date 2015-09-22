try:
    from src.company_class import Company
except ImportError:
    from company_class import Company


def update_class(class_object, properties):
    print("Pressing enter will leave the value unchanged.\n")
    for prop in properties:
        value = getattr(class_object, prop)
        new_value = input("\nCurrent value: {}\nEnter new value: ".format(value))

        if new_value:
            setattr(class_object, prop, new_value)
    print(class_object)


def print_to_screen(list_of_class, verbose=False):
    for index, item in enumerate(list_of_class):
        print("{}: {}\n\n".format(index + 1, item))


if __name__ == "__main__":
    test_class = Company()
    test = test_class.get_all_companies()
    print_to_screen(test)

    #testing = test_class.get_a_company(1)[0]
    #update_class(testing, Company.columns)

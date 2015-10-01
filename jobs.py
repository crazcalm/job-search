import argparse

from src.constants import CHOICES, CHOICES_PLURAL, JOB_POSTINGS
from src.cli_helper import print_to_screen, show, class_factory, get_all_objects_in_db, selection_screen, update_class


def main():
    jobs = argparse.ArgumentParser(description="jobs", epilog="bye")
    jobs.add_argument("-v", action="store_true", help="verbose help")
    group = jobs.add_mutually_exclusive_group()

    group.add_argument("--add", choices=CHOICES, help="add help")
    group.add_argument("--show", choices=CHOICES_PLURAL, help="show help")
    group.add_argument("--update", choices=CHOICES, help="update help")

    cli_args = jobs.parse_args()

    if cli_args.add:
        print("add was selected")
        print("add: ", cli_args.add)
        class_object = class_factory(cli_args.add)

        # Need to figure this out...
        update_class(class_object, class_object.properties)

    elif cli_args.show:
        print("show was selected")
        print("show:", cli_args.show)
        print_to_screen(show(cli_args.show))

    elif cli_args.update:
        print("update was selected")
        print("update:", cli_args.update)
        class_object = class_factory(cli_args.update)
        all_classes = get_all_objects_in_db(class_object)
        wanted_class_object = selection_screen(all_classes)
        update_class(wanted_class_object, wanted_class_object.properties)

    else:
        print("nothing was selected")
        print("I will print out the job postings")
        print_to_screen(show(JOB_POSTINGS))

    print(cli_args)


if __name__ == "__main__":
    main()

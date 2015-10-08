import argparse

from src.constants import CHOICES, CHOICES_PLURAL, JOB_POSTINGS
from src.constants import DESCRIPTION, EPILOG, ADD_HELP, SHOW_HELP, UPDATE_HELP, DELETE_HELP
from src.cli_helper import print_to_screen, show, class_factory, get_all_objects_in_db, selection_screen, update_class
from src.cli_helper import delete_class_object, db_exist, create_db


def main():
    jobs = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)
    #jobs.add_argument("-v", action="store_true", help="verbose help")
    group = jobs.add_mutually_exclusive_group()

    group.add_argument("--add", choices=CHOICES, help=ADD_HELP)
    group.add_argument("--show", choices=CHOICES_PLURAL, help=SHOW_HELP)
    group.add_argument("--update", choices=CHOICES, help=UPDATE_HELP)
    group.add_argument("--delete", choices=CHOICES, help=DELETE_HELP)

    cli_args = jobs.parse_args()

    if cli_args.add:
        class_object = class_factory(cli_args.add)

        # Need to figure this out...
        update_class(class_object, class_object.properties)

    elif cli_args.show:
        objects_to_show = show(cli_args.show)
        if objects_to_show:
            print_to_screen(objects_to_show)
        else:
            print("No {} in the database. Try adding one.".format(cli_args.show))

    elif cli_args.update:
        class_object = class_factory(cli_args.update)
        all_classes = get_all_objects_in_db(class_object)
        wanted_class_object = selection_screen(all_classes)
        update_class(wanted_class_object, wanted_class_object.properties)

    elif cli_args.delete:
        class_object = class_factory(cli_args.delete)
        all_classes = get_all_objects_in_db(class_object)
        wanted_class_object = selection_screen(all_classes)
        delete_class_object(wanted_class_object)

    else:
        objects_to_show = show(JOB_POSTINGS)
        if objects_to_show:
            print_to_screen(objects_to_show)
        else:
            print("No jobpostings in the database. Try adding one.")


if __name__ == "__main__":
    if not db_exist():
        create_db()
    main()

import argparse

from src.constants import CHOICES, CHOICES_PLURAL, JOB_POSTINGS
from src.cli_helper import print_to_screen, show, class_factory, get_all_objects_in_db, selection_screen, update_class
from src.cli_helper import delete_class_object, db_exist, create_db


def main():
    jobs = argparse.ArgumentParser(description="jobs", epilog="bye")
    jobs.add_argument("-v", action="store_true", help="verbose help")
    group = jobs.add_mutually_exclusive_group()

    group.add_argument("--add", choices=CHOICES, help="add help")
    group.add_argument("--show", choices=CHOICES_PLURAL, help="show help")
    group.add_argument("--update", choices=CHOICES, help="update help")
    group.add_argument("--delete", choices=CHOICES, help="delete help")

    cli_args = jobs.parse_args()

    if cli_args.add:
        class_object = class_factory(cli_args.add)

        # Need to figure this out...
        update_class(class_object, class_object.properties)

    elif cli_args.show:
        print_to_screen(show(cli_args.show))

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
        print_to_screen(show(JOB_POSTINGS))


if __name__ == "__main__":
    if not db_exist():
        create_db()
    main()

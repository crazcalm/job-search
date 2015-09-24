import argparse

from src.company_class import Company
from src.contact_class import Contact
from src.recruiter_class import Recruiter
from src.job_posting_class import JobPosting
from src.constants import CHOICES, CHOICES_PLURAL, JOB_POSTINGS

CLASSES = {
    "companies": {
        "class": Company,
        "get_all": "get_all_companies"
    },
    "contacts": {
        "class": Contact,
        "get_all": "get_all_contacts"
    },
    "recruiters": {
        "class": Recruiter,
        "get_all": "get_all_recruiters"
    },
    "job_postings": {
        "class": JobPosting,
        "get_all": "get_all_job_postings"
    }
}



def show(class_type):
    result = None
    if class_type in CLASSES:
        class_info = CLASSES.get(class_type)
        instance = class_info.get("class")()
        result = getattr(instance, class_info.get("get_all"))()
    return result


def print_to_screen(items):
    for index, item in enumerate(items):
        print("{}: {}".format(index, item))


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

    elif cli_args.show:
        print("show was selected")
        print("show:", cli_args.show)
        print_to_screen(show(cli_args.show))

    elif cli_args.update:
        print("update was selected")
        print("update:", cli_args.update)

    else:
        print("nothing was selected")
        print("I will print out the job postings")
        print_to_screen(show(JOB_POSTINGS))

    print(cli_args)


if __name__ == "__main__":
    main()


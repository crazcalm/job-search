import argparse

from src.company_class import Company
from src.contact_class import Contact
from src.recruiter_class import Recruiter
from src.job_posting_class import JobPosting

JOB_POSTING = "job_posting"
RECRUITER = "recruiter"
CONTACT = "contact"
COMPANY = "company"

choices = [COMPANY, CONTACT, RECRUITER, JOB_POSTING]

CLASSES = {
    "company": {
        "class": Company,
        "get_all": "get_all_companies"
    },
    "contact": {
        "class": Contact,
        "get_all": "get_all_contacts"
    },
    "recruiter": {
        "class": Recruiter,
        "get_all": "get_all_recruiters"
    },
    "job_posting": {
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

    group.add_argument("--add", choices=choices, help="add help")
    group.add_argument("--show", choices=choices, help="show help")
    group.add_argument("--update", choices=choices, help="update help")

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
        print_to_screen(show(JOB_POSTING))

    print(cli_args)


if __name__ == "__main__":
    main()


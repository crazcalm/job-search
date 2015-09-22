import argparse

choices = ["company", "contact", "recruiter", "job_posting"]


def main():
    jobs= argparse.ArgumentParser(description="jobs", epilog="bye")
    jobs.add_argument("--foo", action="store_true", help="foo help")
    jobs.add_argument("-v, --verbose", action="store_true", help="verbose help")
    group = jobs.add_mutually_exclusive_group()

    group.add_argument("--add", choices=choices, help="add help")
    group.add_argument("--show", choices=choices, help="show help")
    group.add_argument("--update", choices=choices, help="update help")

    test = jobs.parse_args()
    print(test)


if __name__ == "__main__":
    main()

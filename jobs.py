import argparse

choices = ["company", "contact", "recruiter", "job_posting"]


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

    elif cli_args.update:
        print("update was selected")
        print("update:", cli_args.update)

    else:
        print("nothing was selected")
        print("I will print out the job postings")

    print(cli_args)


if __name__ == "__main__":
    main()

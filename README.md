#Jobs

##Requirements:
	python3.4

##Description:
	This is a command line application geared towards helping you organize your
    job search.

##Install
	git clone git@github.com:crazcalm/job-search.git

#Instructions:
	python3 jobs.py -h

##Interface:
	python3 jobs.py -h
    usage: jobs.py [-h]
    			   [-- add {company, contact, recruiter, jobposting} | --show {companies, contacts, recruiters, jobpostings} | --update {company, contact, recruiter, jobposting} | --delete {company, contacts, recruiter, jobposting}]

	This application allows you to insert job postings into a database.
    Associative information, such as Companies, Contacts, and Recruiters, can be linked to a job posting by reference.
    By default, this application prints all job postings in the database to the screen.

    optional arguments:
    -h, --help			Show this help message and exit
    --add {company, contact, recruiter, jobpostings}
    					Add allows you to add an object to the databse.
	--show {companies, contacts, recruiters, jobpostings}
    					Show prints all of the selected object type to the screen.
	--update {company, contact, recruiter, jobposting}
    					Update allows you to update an object in the databse.
	--delete {company, contact, recruiter, jobposting}
    					Delete allows you to delete an object in the database.

	Source code can be found at https://github.com/crazcalm/job-search
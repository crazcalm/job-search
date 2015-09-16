import os

# test database
TEST_DB = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "SQL_files", "test.db"))
SQL_FILES = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "SQL_files"))


# DB creatation sql statments
COMPANY_DB = {
    "table": "DROP TABLE IF EXISTS company;",
    "columns": """
    CREATE TABLE company(
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL DEFAULT "",
    address     TEXT NOT NULL DEFAULT "",
    website     TEXT NOT NULL DEFAULT "",
    phone       TEXT NOT NULL DEFAULT ""
        );
    """
}

CONTACTS_DB = {
    "table": "DROP TABLE IF EXISTS contacts;",
    "columns": """
    CREATE TABLE contacts(
    id                  INTEGER PRIMARY KEY,
    first_name          TEXT NOT NULL DEFAULT "",
    last_name           TEXT NOT NULL DEFAULT "",
    email               TEXT NOT NULL DEFAULT "",
    phone               TEXT NOT NULL DEFAULT "",
    description         TEXT NOT NULL DEFAULT "",
    companyId           INTEGER,
    FOREIGN KEY (companyId) REFERENCES company(id) ON DELETE CASCADE ON UPDATE CASCADE
        );
    """
}

RECRUITERS_DB = {
    "tables": "DROP TABLE IF EXISTS recruiters;",
    "columns": """
    CREATE TABLE recruiters(
    id                  INTEGER PRIMARY KEY,
    first_name          TEXT NOT NULL DEFAULT "",
    last_name           TEXT NOT NULL DEFAULT "",
    email               TEXT NOT NULL DEFAULT "",
    phone               TEXT NOT NULL DEFAULT "",
    description         TEXT NOT NULL DEFAULT "",
    companyId           INTEGER,
    FOREIGN KEY (companyId) REFERENCES company(id) ON DELETE CASCADE ON UPDATE CASCADE
        );
    """
}

JOB_POSTING_DB = {
    "table": "DROP TABLE IF EXISTS job_posting;",
    "columns": """
    CREATE TABLE job_posting(
    id                  INTEGER PRIMARY KEY,
    link                TEXT NOT NULL DEFAULT "",
    date_applied        TEXT NOT NULL DEFAULT "",
    description         TEXT NOT NULL DEFAULT "",
    interviewed         TEXT NOT NULL DEFAULT "",
    companyId           INTEGER,
    recruiterId         INTEGER,
    contactId           INTEGER,
    FOREIGN KEY(companyId)      REFERENCES company(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(recruiterId)    REFERENCES recruiters(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(contactId)      REFERENCES contacts(id) ON DELETE CASCADE ON UPDATE CASCADE
        );
    """

}

# The order does matter.
DB_TABLE_CREATION = [COMPANY_DB, CONTACTS_DB, RECRUITERS_DB, JOB_POSTING_DB]

# Test data:
COMPANY_DATA = [
    ('INSERT INTO company (name, address, website, phone) VALUES ("Google", "Somewhere in Cali",'
     ' "Google.com", "555-555-5555");'),
    ('INSERT INTO company (name, address, website, phone) VALUES ("Yahoo", "Also in Cali",'
     ' "Yahoo.com", "666-666-6666");'),
    ('INSERT INTO company (name, address, website, phone) VALUES ("IBM", "Cali Cali",'
     ' "IBM.com", "777-777-7777");'),
    ('INSERT INTO company (name, address, website, phone) VALUES ("Bing", "Cali",'
     ' "Bing.com", "888-888-8888");'),
    ('INSERT INTO company (name, address, website, phone) VALUES ("Crazcalm", "NYC",',
     ' "Crazcalm.com", "999-999-9999");')
]

CONTACTS_DATA = [
    ('INSERT INTO contacts (last_name, first_name, email, phone, description)'
     ' VALUES ("Willock", "Marcus", "crazcalm@gmail.com", "6023417413", "It\'s Me!");'),
    'INSERT INTO contacts (last_name, first_name) VALUES ("Teran", "Jovanna");',
    'INSERT INTO contacts (last_name, first_name) VALUES ("Donuts", "Dunkin");',
    'INSERT INTO contacts (last_name) VALUES ("Allen");',
    'INSERT INTO contacts (last_name) VALUES ("Price");'
]

RECRUITERS_DATA = [
    ('INSERT INTO recruiters (first_name, last_name, email, phone, companyId) VALUES ("Recuiter1",'
     ' "1Recruiter", "recruiter1@gmail.com", "111-111-1111", 1);'),
    ('INSERT INTO recruiters (first_name, last_name, email, phone, companyId) VALUES ("Recuiter2",'
     ' "2Recruiter", "recruiter2@gmail.com", "222-222-2222", 4);'),
    ('INSERT INTO recruiters (first_name, last_name, email, phone, companyId) VALUES ("Recuiter3",'
     ' "3Recruiter", "recruiter3@gmail.com", "333-333-3333", 1);'),
    ('INSERT INTO recruiters (first_name, last_name, email, phone, companyId) VALUES ("Recuiter4",'
     ' "4Recruiter", "recruiter4@gmail.com", "444-444-4444", 3);'),
    ('INSERT INTO recruiters (first_name, last_name, email, phone, companyId) VALUES ("Recuiter5",'
     ' "5Recruiter", "recruiter5@gmail.com", "555-555-5555", 2);'),
    ('INSERT INTO recruiters (first_name, last_name, email, phone, companyId) VALUES ("Recuiter6",'
     ' "6Recruiter", "recruiter6@gmail.com", "666-666-6666", 1);'),
    ('INSERT INTO recruiters (first_name, last_name, email, phone, companyId) VALUES ("Recuiter7",'
     ' "7Recruiter", "recruiter7@gmail.com", "777-777-7777", 1);')
]

JOB_POSTING_DATA = [
    ('INSERT INTO job_posting (link, date_applied, description, interviewed, companyId,'
     ' recruiterId, contactId) VALUES ("www.link.com", "DATE1", "Description",'
     ' "yep", 1, 1, 1);')
]

DB_TEST_DATA = [COMPANY_DATA, CONTACTS_DATA, RECRUITERS_DATA, JOB_POSTING_DATA]

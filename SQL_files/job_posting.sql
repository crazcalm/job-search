DROP TABLE IF EXISTS job_posting;
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
    FOREIGN KEY(recruiterId)    REFERENCES recruiter(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(contactId)      REFERENCES contact(id) ON DELETE CASCADE ON UPDATE CASCADE
);
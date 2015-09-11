DROP TABLE IF EXISTS job_posting;
CREATE TABLE job_posting(
    id                  INTEGER PRIMARY KEY,
    link                TEXT NOT NULL DEFAULT "",
    date_applied        TEXT NOT NULL DEFAULT "",
    description         TEXT NOT NULL DEFAULT "",
    interviewed         TEXT NOT NULL DEFAULT "",
    company             TEXT NOT NULL DEFAULT "",
    recruiter           TEXT NOT NULL DEFAULT "",
    contact             TEXT NOT NULL DEFAULT ""
);
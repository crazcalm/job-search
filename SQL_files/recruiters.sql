DROP TABLE IF EXISTS recruiters;
CREATE TABLE recruiters(
    id                  INTEGER PRIMARY KEY,
    first_name          TEXT NOT NULL DEFAULT "",
    last_name           TEXT NOT NULL DEFAULT "",
    email               TEXT NOT NULL DEFAULT "",
    phone               TEXT NOT NULL DEFAULT "",
    companyId           INTEGER,
    job_postingId       INTEGER,
    FOREIGN KEY (companyId) REFERENCES company(id) ON DEFAULT CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (job_postingId) REFERENCES job_posting(id) ON DEFAULT CASCADE ON UPDATE CASCADE
);
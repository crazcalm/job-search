DROP TABLE IF EXISTS recruiters;
CREATE TABLE recruiters(
    id                  INTEGER PRIMARY KEY,
    first_name          TEXT NOT NULL DEFAULT "",
    last_name           TEXT NOT NULL DEFAULT "",
    email               TEXT NOT NULL DEFAULT "",
    phone               TEXT NOT NULL DEFAULT "",
    company             TEXT NOT NULL DEFAULT ""
)
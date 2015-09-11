DROP TABLE IF EXISTS contacts;
CREATE TABLE contacts(
    id                  INTEGER PRIMARY KEY,
    first_name          TEXT NOT NULL DEFAULT "",
    last_name           TEXT NOT NULL DEFAULT "",
    email               TEXT NOT NULL DEFAULT "",
    phone               TEXT NOT NULL DEFAULT "",
    description         TEXT NOT NULL DEFAULT ""
);
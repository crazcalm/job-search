DROP TABLE IF EXISTS company;
CREATE TABLE company(
    id          INTEGER PRIMARY KEY,
    name        TEXT NOT NULL DEFAULT "",
    address     TEXT NOT NULL DEFAULT "",
    website     TEXT NOT NULL DEFAULT "",
    phone       TEXT NOT NULL DEFAULT ""
);
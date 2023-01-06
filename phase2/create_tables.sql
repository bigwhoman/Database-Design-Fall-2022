-- Active: 1671320079078@@127.0.0.1@5433@postgres@public


CREATE TABLE Customer (
    customerId INTEGER NOT NULL,
    firstName TEXT,
    lastName TEXT,
    addr TEXT,
    age INTEGER,
    sex CHAR,
    credit INTEGER,
    PRIMARY KEY (customerId)
);

SELECT * FROM customer;
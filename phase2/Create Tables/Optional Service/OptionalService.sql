-- Active: 1671320079078@@127.0.0.1@5433@postgres@public


CREATE TABLE OptionalService (
    ServiceName TEXT NOT NULL,
    cost INTEGER,
    PRIMARY KEY (ServiceName)
);

SELECT * FROM OptionalService;
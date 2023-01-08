-- Active: 1671320079078@@127.0.0.1@5433@postgres@public
CREATE TABLE
    DamageReport (damageCost INTEGER, description TEXT) INHERITS(Report);

INSERT INTO DamageReport
VALUES (22,4,2,'2023-01-03',2000,'ded'),(23,4,5,'2023-01-03',300,'ded'),(24,1,9,'2023-01-03',10,'ded'),(25,2,7,'2023-01-03',80000,'ded');

select * from damagereport;

select * from contract where id = 30; 

select * from report;
CREATE VIEW DAMAGECUSTOMERS 
	AS
	SELECT
	    firstname,
	    lastname,
	    national_number,
	    salon_id,
	    safebox_number
	FROM damagereport
	    JOIN contract ON damagereport.contractId = contract.id
	    JOIN customer ON customer.customerid = contract.customer_id
; 

select * from contract;

ALTER TABLE customer
ADD
    column national_number INTEGER NOT NULL default (random() * 200000) :: INTEGER;

ALTER TABLE customer DROP column national_number;

SELECT * FROM customer;
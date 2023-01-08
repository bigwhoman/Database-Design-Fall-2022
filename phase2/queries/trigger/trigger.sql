CREATE OR REPLACE FUNCTION seeIfAccLimit()
  RETURNS trigger AS
$func$
BEGIN
   IF ( (SELECT Count(*) FROM Account WHERE Account.customer_id = NEW.customer_id)>=5)
     THEN
      RAISE EXCEPTION 'Cannot Insert -- Maximum Accounts Reached';
   END IF;
   RETURN NEW;
END
$func$  LANGUAGE plpgsql;

	CREATE TRIGGER ACCOUNTLIMIT 
		before
		INSERT ON Account FOR EACH ROW
		EXECUTE
		    PROCEDURE seeIfAccLimit();
	; 
	ALTER TABLE Account ENABLE TRIGGER ALL;

    DROP TRIGGER ACCOUNTLIMIT
ON Account;



INSERT INTO Account VALUES(21,1);
INSERT INTO Account VALUES(21,2);
INSERT INTO Account VALUES(21,3);
INSERT INTO Account VALUES(21,4);
INSERT INTO Account VALUES(21,5);
INSERT INTO Account VALUES(21,6);
select * from account;

DELETE FROM Customer WHERE customerid = 21;

INSERT INTO customer (customerid,national_number) VALUES (21,1234567);

Select * from customer;
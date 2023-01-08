PREPARE getEnterReports(INT) 
AS
SELECT * FROM EnterReport WHERE customer_id = $1;

EXECUTE getEnterReports(18);
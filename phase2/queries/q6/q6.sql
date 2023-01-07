PREPARE MAX_TIME(INT, INT)
AS
SELECT credit/(SELECT min(dailyCost) FROM 
SafeBox JOIN Salon on safebox.salonId = salon.salonId NATURAL JOIN securitylevel NATURAL JOIN pricegroup
WHERE level = $1 and credit >= max_value) AS MAX_DAYS
FROM customer where customerid = $2;

EXECUTE MAX_TIME(2,12);

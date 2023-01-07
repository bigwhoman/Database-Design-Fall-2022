PREPARE getFreeBoxRent(INTEGER,INTEGER) AS
SELECT safebox.salonId,safebox.safebox_number
FROM safebox
    LEFT JOIN salon ON safebox.salonId = salon.salonid
    LEFT JOIN contract ON 
        contract.safebox_number = safebox.safebox_number 
        AND contract.salon_id = salon.salonId
    WHERE customer_id is NULL
    AND salon.securitylevelid = $1 AND pricegroup <= $2;

EXECUTE  getFreeBoxRent(1,20);

DEALLOCATE getFreeBoxRent;


SELECT * FROM salon JOIN safebox ON safebox.salonid = salon.salonid
WHERE securitylevelid = 1;
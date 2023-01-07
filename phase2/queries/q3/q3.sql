PREPARE getCommercialAvg(INTEGER,INTEGER) AS
    SELECT AVG(age)
    FROM bcustomer
        JOIN contract ON contract.customer_id = bcustomer.customerid
        JOIN salon ON salon.salonId = contract.salon_id
    WHERE
        salon.salonId = $1
        AND commercial_suggest = $2;


EXECUTE getCommercialAvg(1,12);
DEALLOCATE getCommercialAvg;
SELECT * FROM bcustomer;
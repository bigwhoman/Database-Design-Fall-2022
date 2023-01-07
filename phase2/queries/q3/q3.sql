SELECT AVG(age)
FROM bcustomer
    JOIN contract ON contract.customer_id = bcustomer.customerid
    JOIN salon ON salon.salonId = contract.salon_id
WHERE
    salon.salonId = 2
    AND commercial_suggest = 1;
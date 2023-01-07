SELECT AVG(age)
FROM bcustomer
    JOIN contract ON contract.customer_id = bcustomer.customerid
    JOIN salon ON salon.salonId = contract.salon_id
WHERE
    salon.salonId = room_id
    AND commercial_suggest = plan_id;
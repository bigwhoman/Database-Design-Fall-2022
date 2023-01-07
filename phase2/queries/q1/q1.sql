SELECT securityLevelId
FROM customer
    JOIN contract ON customer.customerId = contract.customer_id
    JOIN salon ON salon.salonId = contract.salon_id
WHERE customer.customerid = usr_id;
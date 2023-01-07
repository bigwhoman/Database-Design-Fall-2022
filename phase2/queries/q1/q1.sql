PREPARE
    getCustomerBox(INTEGER) AS
SELECT
    salon.salonid,
    contract.safebox_number,
    securityLevelId
FROM customer
    JOIN contract ON customer.customerId = contract.customer_id
    JOIN salon ON salon.salonId = contract.salon_id
WHERE customer.customerid = $1;

EXECUTE getCustomerBox(3);

DEALLOCATE getCustomerBox;

SELECT * FROM contract
customer_id = 3;
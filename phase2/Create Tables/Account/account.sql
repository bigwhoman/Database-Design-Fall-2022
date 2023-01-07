CREATE TABLE Account(
    customer_id INT NOT NULL,
    id INT NOT NULL,
    FOREIGN KEY(customer_id) 
    REFERENCES Customer(customerId) on delete CASCADE,
    PRIMARY KEY(id, customer_id)
);

SELECT * FROM Account;
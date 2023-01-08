CREATE TABLE EnterReport(
    customer_id INT,
    salon_id INT,
    safebox_number INT,
    time TIMESTAMP,
    PRIMARY KEY(customer_id,salon_id,safebox_number,time),
    FOREIGN KEY(customer_id) REFERENCES Customer(customerId) on delete CASCADE,
    FOREIGN KEY(salon_id, safebox_number) REFERENCES SafeBox(salonId, safebox_number) on delete CASCADE
);
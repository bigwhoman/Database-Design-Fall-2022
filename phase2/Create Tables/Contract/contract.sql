-- Active: 1671320079078@@127.0.0.1@5433@postgres@public
CREATE TABLE Contract (
    id INT NOT NULL PRIMARY KEY,
    customer_id INT NOT NULL,
    safebox_number INT NOT NULL,
    salon_id INT NOT NULL,
    time_schedule INT NOT NULL,
    startTime TIMESTAMP NOT NULL,
    paid_amount INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customer (customerId) ON DELETE CASCADE,
    FOREIGN KEY (time_schedule) REFERENCES TimeSchedule (length) ON DELETE CASCADE,
    FOREIGN KEY (safebox_number,salon_id) REFERENCES SafeBox (safebox_number, salonID) ON DELETE CASCADE,
    FOREIGN KEY (salon_id) REFERENCES Salon (salonID) ON DELETE CASCADE
);
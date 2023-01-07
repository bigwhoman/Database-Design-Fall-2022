CREATE TABLE SafeBox (
    safebox_number INTEGER NOT NULL,
    salonID INTEGER NOT NULL,
    priceGroup INTEGER,
    PRIMARY KEY (safebox_number,salonID),
    FOREIGN KEY (priceGroup) REFERENCES PriceGroup(dailyCost)
);

SELECT * FROM Safebox;
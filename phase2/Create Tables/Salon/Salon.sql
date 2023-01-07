CREATE TABLE Salon (
    salonID INTEGER NOT NULL,
    cameras INTEGER,
    boxCount INTEGER,
    wall INTEGER,
    securityLevelId INTEGER,
    employeeId INTEGER,
    PRIMARY KEY (salonID),
    FOREIGN KEY (securityLevelId) REFERENCES SecurityLevel(level),
    FOREIGN KEY (employeeId) REFERENCES Employee(id)
    
);

SELECT * FROM Salon;
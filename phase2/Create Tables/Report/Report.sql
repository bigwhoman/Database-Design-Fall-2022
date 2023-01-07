CREATE TABLE Report(
    ReportID INTEGER NOT NULL,
    safeboxID INTEGER,
    salonID INTEGER,
    employeeID INTEGER,
    ContractID INTEGER,
    time DATE
    PRIMARY KEY(ReportID),
    FOREIGN KEY(employeeID) REFERENCES Employee(id),
    FOREIGN KEY(safeboxID,salonID) REFERENCES safebox(safebox_number,salonID), --> ???????
    FOREIGN KEY(contractID) REFERENCES 
    
);

SELECT * FROM Report;
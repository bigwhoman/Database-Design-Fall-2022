CREATE TABLE Report(
    ReportID INTEGER NOT NULL,
    safeboxID INTEGER,
    employeeID INTEGER,
    ContractID INTEGER,
    time DATE
    PRIMARY KEY(ReportID),
    FOREIGN KEY(employeeID) REFERENCES Employee(id),
    FOREIGN KEY(safeboxID) REFERENCES safebox(safebox_number), --> ???????
    FOREIGN KEY(contractID) REFERENCES 
    
);

SELECT * FROM Report;
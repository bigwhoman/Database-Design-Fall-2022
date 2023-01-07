CREATE TABLE Report(
    ReportID INTEGER NOT NULL,
    employeeID INTEGER,
    ContractID INTEGER,
    time DATE,
    PRIMARY KEY(ReportID),
    FOREIGN KEY(employeeID) REFERENCES Employee(id),
    FOREIGN KEY(contractID) REFERENCES Contract(id)
    
);

SELECT * FROM Report;
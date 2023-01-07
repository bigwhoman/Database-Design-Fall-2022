CREATE TABLE BCustomer(
    commercial_suggest INT NOT NULL,
    FOREIGN KEY(commercial_suggest) 
    REFERENCES CommercialSuggest(offPercent) on delete CASCADE 
) INHERITS(Customer);

SELECT * FROM BCustomer;
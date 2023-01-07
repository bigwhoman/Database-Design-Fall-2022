
PREPARE getEmployee(INTEGER,INTEGER) AS
    SELECT
        employee.personaldata,
        employee.salary
    FROM employee
        JOIN salon ON salon.employeeId = employee.id
    WHERE
        salon.securityLevelId BETWEEN $1 AND $2
    ORDER BY RANDOM();

EXECUTE getEmployee(3,5);
DEALLOCATE getEmployee;

SELECT * FROM employee JOIN salon ON salon.employeeid = employee.id;
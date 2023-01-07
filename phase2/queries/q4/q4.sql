

SELECT
    employee.personaldata,
    employee.salary
FROM employee
    JOIN salon ON salon.employeeId = employee.id
WHERE
    salon.securityLevelId BETWEEN from_level AND to_level
ORDER BY RANDOM();


-- PREPARE foo(INTEGER) AS
--     SELECT  * 
--     FROM    customer
--     WHERE   customerid = $1 ;
-- EXECUTE foo(5);
-- DEALLOCATE foo;
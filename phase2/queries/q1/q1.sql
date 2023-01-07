DECLARE @Parameter VARCHAR(20)
SET @Parameter = 'John';

SELECT *
FROM Table node
WHERE Name = @Parameter;

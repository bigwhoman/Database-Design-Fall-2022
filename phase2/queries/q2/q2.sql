PREPARE getRent(INTEGER,INTEGER) AS
    SELECT safebox_number,safebox.salonid,(30 * $2 * pricegroup) AS Rent_Per_Months FROM 
    salon JOIN safebox ON safebox.salonID=salon.salonID
    WHERE securitylevelid = $1;

-- getRent(level,month)
EXECUTE getRent(1,2);
DEALLOCATE getRent;
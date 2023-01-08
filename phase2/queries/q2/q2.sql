-- Active: 1671320079078@@127.0.0.1@5433@postgres@public
PREPARE getRent(INTEGER,INTEGER) AS
    SELECT safebox_number,safebox.salonid,(30 * $2 * pricegroup) AS Rent_Per_Months FROM 
    salon JOIN safebox ON safebox.salonID=salon.salonID
    WHERE securitylevelid = $1;

-- getRent(level,month)

EXECUTE getRent(1,2);
DEALLOCATE getRent;

CREATE UNIQUE INDEX salonINDX ON salon(salonID);
CREATE UNIQUE INDEX lvlINDX ON SecurityLevel(level);
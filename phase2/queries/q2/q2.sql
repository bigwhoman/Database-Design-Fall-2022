SELECT safebox_number,safebox.salonid,(30 * months * pricegroup) AS Rent_Per_Months FROM 
salon JOIN safebox ON safebox.salonID=salon.salonID
WHERE securitylevelid = level;
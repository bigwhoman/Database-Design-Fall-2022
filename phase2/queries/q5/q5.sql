SELECT salon_id,contract.safebox_number
FROM safebox
    LEFT JOIN salon ON safebox.salonId = salon.salonid
    LEFT JOIN contract ON 
        contract.safebox_number = safebox.safebox_number 
        AND contract.salon_id = salon.salonId
    WHERE customer_id is NULL
    AND salon.securitylevelid = level AND pricegroup <= max_price; 
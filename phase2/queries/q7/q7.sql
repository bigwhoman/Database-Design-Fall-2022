select safebox_number, salon_id, starttime, length from contract JOIN TimeSchedule ON time_schedule = length
where starttime + interval '1 month' * length <= NOW();
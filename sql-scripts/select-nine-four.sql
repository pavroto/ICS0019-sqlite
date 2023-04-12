SELECT Name, time_open, time_closed
FROM CANTEEN
WHERE time_open <= TIME('09:00') AND time_closed >= TIME('16:20');

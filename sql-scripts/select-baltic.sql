SELECT c.Name, p.ProviderName, c.time_open, c.time_closed
FROM CANTEEN C
CROSS JOIN PROVIDER P
ON P.ID = C.ProviderID
WHERE P.ProviderName='Baltic Restaurants Estonia AS';
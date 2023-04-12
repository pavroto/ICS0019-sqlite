INSERT INTO CANTEEN
(ProviderID, Name, Location, time_open, time_closed)
VALUES
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Rahva Toit"),
    "Economics- and social science building canteen",
    "Akadeemia tee 3",
    strftime('8:30'),
    strftime('18:30')
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Rahva Toit"),
    "Library canteen",
    "Akadeemia tee 1/Ehitajate tee 7",
    strftime('8:30'),
    strftime('19:00')
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Baltic Restaurants Estonia AS"),
    "Main building Deli cafe",
    "Ehitajate tee 5",
    strftime('9:00'),
    strftime('16:30')
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Baltic Restaurants Estonia AS"),
    "Main building Daily lunch restaurant",
    "Ehitajate tee 5",
    strftime('9:00'),
    strftime('16:30')
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Rahva Toit"),
    "U06 building canteen",
    NULL,
    strftime('9:00'),
    strftime('16:00')
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Baltic Restaurants Estonia AS"),
    "Natural Science building canteen",
    "Akadeemia tee 15",
    strftime('9:00'),
    strftime('16:00')
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Baltic Restaurants Estonia AS"),
    "ICT building canteen",
    "Raja 15/Mäepealse 1",
    strftime('9:00'),
    strftime('16:00')
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="TTÜ Sport"),
    "Sports building canteen",
    "Männiliiva 7",
    strftime('11:00'),
    strftime('20:00')
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Bitstop Kohvik OÜ"),
    "bitStop KOHVIK",
    "IT College, Raja 4c",
    strftime('9:30'),
    strftime('16:00')
);
INSERT INTO CANTEEN
(ProviderID, Name, Location, time_open, time_closed)
VALUES
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Rahva Toit"),
    "Economics- and social science building canteen",
    "Akadeemia tee 3",
    '08:30',
    '18:30'
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Rahva Toit"),
    "Library canteen",
    "Akadeemia tee 1/Ehitajate tee 7",
    '08:30',
    '19:00'
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Baltic Restaurants Estonia AS"),
    "Main building Deli cafe",
    "Ehitajate tee 5",
    '09:00',
    '16:30'
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Baltic Restaurants Estonia AS"),
    "Main building Daily lunch restaurant",
    "Ehitajate tee 5",
    '09:00',
    '16:30'
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Rahva Toit"),
    "U06 building canteen",
    NULL,
    '09:00',
    '16:00'
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Baltic Restaurants Estonia AS"),
    "Natural Science building canteen",
    "Akadeemia tee 15",
    '09:00',
    '16:00'
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Baltic Restaurants Estonia AS"),
    "ICT building canteen",
    "Raja 15/Mäepealse 1",
    '09:00',
    '16:00'
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="TTÜ Sport"),
    "Sports building canteen",
    "Männiliiva 7",
    '11:00',
    '20:00'
),
(
    (SELECT ID FROM PROVIDER WHERE ProviderName="Bitstop Kohvik OÜ"),
    "bitStop KOHVIK",
    "IT College, Raja 4c",
    '09:30',
    '16:00'
);
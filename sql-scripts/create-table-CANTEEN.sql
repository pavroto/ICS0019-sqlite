CREATE TABLE CANTEEN
(
    ID INTEGER PRIMARY KEY ASC,
    ProviderID INTEGER,
    Name TEXT,
    Location,
    time_open,
    time_closed

    FOREIGN KEY(ProviderID) REFERENCES PROVIDER(ID)
);
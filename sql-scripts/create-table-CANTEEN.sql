CREATE TABLE CANTEEN
(
    ID INTEGER PRIMARY KEY ASC,
    ProviderID INTEGER,
    Name TEXT,
    Location TEXT,
    time_open TIME,
    time_closed TIME,
    FOREIGN KEY(ProviderID) REFERENCES PROVIDER(ID)
);
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Time, type_coerce
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import join
from sqlalchemy.sql import select

from datetime import time

DATABASE_NAME = "DINERS-Alchemy.db"

f = open(DATABASE_NAME, "w")  # recreate .db file
f.close()

# Create Database
engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Base = declarative_base()


class Provider(Base):
    __tablename__ = 'PROVIDER'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    ProviderName = Column(String)


class Canteen(Base):
    __tablename__ = 'CANTEEN'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    ProviderID = Column(Integer, ForeignKey("PROVIDER.ID"), nullable=False)
    Name = Column(String)
    Location = Column(String)
    time_open = Column(Time)
    time_closed = Column(Time)


Base.metadata.create_all(engine)


# Insert Data
def return_provider_id(provider_name):
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        result = session.query(Provider).filter_by(ProviderName=provider_name)
    except:
        session.rollback()
        raise
    finally:
        session.close()

    for row in result:
        return row.ID


conn = engine.connect()
conn.execute(
    Provider.__table__.insert(),
    [
        {"ProviderName": "Rahva Toit"},
        {"ProviderName": "Baltic Restaurants Estonia AS"},
        {"ProviderName": "TTÜ Sport"},
        {"ProviderName": "Bitstop Kohvik OÜ"}
    ]
)
conn.commit()

conn.execute(
    Canteen.__table__.insert(),
    [
        {
            "ProviderID": return_provider_id('Rahva Toit'),
            "Name": "Economics- and social science building canteen",
            "Location": "Akadeemia tee 3",
            "time_open": time(8, 30),
            "time_closed": time(18, 30)
        },
        {
            "ProviderID": return_provider_id('Rahva Toit'),
            "Name": "Library canteen",
            "Location": "Akadeemia tee 1/Ehitajate tee 7",
            "time_open": time(8, 30),
            "time_closed": time(19,0)
        },
        {
            "ProviderID": return_provider_id('Baltic Restaurants Estonia AS'),
            "Name": "Main building Deli cafe",
            "Location": "Ehitajate tee 5",
            "time_open": time(9, 0),
            "time_closed": time(16, 30)
        },
        {
            "ProviderID": return_provider_id('Baltic Restaurants Estonia AS'),
            "Name": "Main building Daily lunch restaurant",
            "Location": "Ehitajate tee 5",
            "time_open": time(9, 0),
            "time_closed": time(16, 30)
        },
        {
            "ProviderID": return_provider_id('Rahva Toit'),
            "Name": "U06 building canteen",
            "Location":None,
            "time_open": time(9, 0),
            "time_closed": time(16, 0)
        },
        {
            "ProviderID": return_provider_id('Baltic Restaurants Estonia AS'),
            "Name": "Natural Science building canteen",
            "Location": "Akadeemia tee 15",
            "time_open": time(9, 0),
            "time_closed": time(16, 0)
        },
        {
            "ProviderID": return_provider_id('Baltic Restaurants Estonia AS'),
            "Name": "ICT building canteen",
            "Location": "Raja 15/Mäepealse 1",
            "time_open": time(9, 0),
            "time_closed": time(16, 0)
        },
        {
            "ProviderID": return_provider_id('TTÜ Sport'),
            "Name": "Sports building canteen",
            "Location": "Männiliiva 7",
            "time_open": time(11, 0),
            "time_closed": time(20, 0)
        },
        {
            "ProviderID": return_provider_id('Bitstop Kohvik OÜ'),
            "Name": "bitStop KOHVIK",
            "Location": "IT College, Raja 4c",
            "time_open": time(9, 30),
            "time_closed": time(16, 0)
        },

    ]
)
conn.commit()
conn.close()

# Select Data todo

def select_nine_four():
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        result = session.query(Canteen).filter(type_coerce(Canteen.time_open, Time) <= time(9,0), type_coerce(Canteen.time_closed, Time) >= time(16,20))
    except:
        session.rollback()
        raise
    finally:
        session.close()

    for row in result:
        print(row.ID, "|", row.Name, "|", row.time_open, "|", row.time_closed)


def select_baltic():
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        result = session.query(Canteen, Provider).join(Provider, Canteen.ProviderID==Provider.ID).filter_by(ProviderName="Baltic Restaurants Estonia AS")
    except:
        session.rollback()
        raise
    finally:
        session.close()

    for row in result:
        print(row.Canteen.ID, "|", row.Canteen.Name, "|", row.Provider.ProviderName, "|", row.Canteen.time_open, "|", row.Canteen.time_closed)


select_nine_four()
print()
select_baltic()

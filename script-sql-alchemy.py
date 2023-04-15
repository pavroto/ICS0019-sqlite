from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

DATABASE_NAME = "DINERS-Alchemy.db"

engine = create_engine(f'sqlite:///{DATABASE_NAME}')
Base = declarative_base()


class Provider(Base):
    __tablename__ = 'PROVIDER'

    ID = Column(Integer, primary_key=True)
    ProviderName = Column(String)


class Canteen(Base):
    __tablename__ = 'CANTEEN'

    ID = Column(Integer, primary_key=True)
    ProviderID = Column(Integer, ForeignKey("PROVIDER.ID"), nullable=False)
    Name = Column(String)
    Location = Column(String)
    time_open = Column(Time)
    time_closed = Column(Time)
    provider = relationship("Provider", back_populates="CANTEEN")


Provider.canteens = relationship("Canteen", order_by=Canteen.ID, back_populates="provider")
Base.metadata.create_all(engine)


from sqlalchemy import Boolean, Integer, Column, ForeignKey, String
from connect import Base

class Airplane(Base):
    __tablename__="Airplane"
    airplane_id = Column(Integer, primary_key=True, index=True)
    number_of_seats = Column(Integer)
    range_km = Column(Integer)
    model_name = Column(String(255))

class Flight(Base):
    __tablename__ ="Flight"
    flight_number = Column(String(255), primary_key=True, index=True)
    airplane_id = Column(Integer, ForeignKey("airplane_id"))
    datetime_stamp = Column(String(255))
    from_city = Column(String(255))
    to_city = Column(String(255))

class Passenger(Base):
    __tablename__ ="Passenger"
    passenger_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    seat_number = Column(String(255))
    flight_number = Column(String(255), ForeignKey("Flight.flight_number"))


from pydantic import BaseModel
from datetime import datetime

class AirplaneBase(BaseModel):
    number_of_seats: int
    range_km: int
    model_name: str

class AirplaneCreate(AirplaneBase):
    pass

class AirplaneGet(AirplaneBase):
    airplane_id: int

class FlightBase(BaseModel):
    flight_number: str
    airplane_id: int
    datetime_stamp: datetime
    from_city: str
    to_city: str

class FlightCreate(FlightBase):
    pass

class FlightGet(FlightBase):
    pass

class PassengerBase(BaseModel):
    name: str
    seat_number: str
    flight_number: str

class PassengerCreate(PassengerBase):
    passenger_id: str

class PassengerGet(PassengerBase):
    passenger_id: str

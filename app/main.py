from sqlalchemy.orm import Session
import models, crud, schemas
from connect import SessionLocal, engine


# models.Base.metadata.create_all(bind=engine)
# List all the car owners (5)
# List all cars from a specific year (10
# What is the most expensive service? (10)
#What is the average price of all services? (10) 
# Add a Tire Rotation service for all cars that have more than 32000km (20)
# There has been a recall on air filters, provide the last name and the phone number of all owners who had an Air filter replacement. (25)



def get_Flight_by_date(date: str):
    db = SessionLocal()
    user = crud.get_user(db=db, user_id=date)
    db.close()
    return user





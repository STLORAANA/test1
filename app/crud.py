import models, schemas
from sqlalchemy.orm import Session

def get_user(db: Session, user_id: str):
    return db.query(models.Flight).filter(models.Flight.datetime_stamp == user_id).first()

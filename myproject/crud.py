from sqlalchemy.orm import Session
import models
import schemas


def get_country(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.id == country_id).first()


def get_country_by_name(db: Session, name: str):
    return db.query(models.Country).filter(models.Country.name == name).first()


def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()

def create_country(db: Session, country: schemas.CountryCreate):
    db_Country = models.Country(name=country.name, population=country.population)
    db.add(db_Country)
    db.commit()
    db.refresh(db_Country)
    return db_Country


def get_civilians(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.People).offset(skip).limit(limit).all()

def create_country_civilians(db: Session, civilians: schemas.PeopleCreate, country_id: int):
    db_people = models.People(**civilians.dict(), country_id=country_id)
    db.add(db_people)
    db.commit()
    db.refresh(db_people)
    return db_people

def update_country(db: Session, country_id: int, updated_country: schemas.CountryCreate):
    db_country = db.query(models.Country).filter(models.Country.id == country_id).first()
    if db_country:
        for key, value in updated_country.dict().items():
            setattr(db_country, key, value)
        db.commit()
        db.refresh(db_country)
        return db_country

def delete_country(db: Session, country_id: int):
    db_country = db.query(models.Country).filter(models.Country.id == country_id).first()
    if db_country:
        db.delete(db_country)
        db.commit()
        return db_country

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()
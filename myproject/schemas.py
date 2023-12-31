from pydantic import BaseModel


class PeopleBase(BaseModel):
    surname: str
    lastname: str
    email: str

class PeopleCreate(PeopleBase):
    pass

class People(PeopleBase):
    id: int
    country_id: int

    class Config:
        orm_mode = True

class CityBase(BaseModel):
    name: str
    population: int

class CountryBase(BaseModel):
    name: str

class CountryCreate(CountryBase):
    population: int

class Country(CountryBase):
    id: int
    civilians: list[People] = []

    class Config:
        orm_mode = True
class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True


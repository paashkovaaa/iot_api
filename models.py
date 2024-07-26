import os

from dotenv import load_dotenv
from peewee import *

load_dotenv()

db = PostgresqlDatabase(
    os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("HOST"),
    port="5432",
)


class BaseModel(Model):
    class Meta:
        database = db


class ApiUser(BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()


class Location(BaseModel):
    name = CharField(unique=True)


class Device(BaseModel):
    name = CharField(unique=True)
    type = CharField()
    login = CharField(unique=True)
    password = CharField()
    location_id = ForeignKeyField(Location, backref="devices")
    api_user_id = ForeignKeyField(ApiUser, backref="devices")


def initialize_db():
    db.connect()
    db.create_tables([ApiUser, Location, Device])

    db.close()

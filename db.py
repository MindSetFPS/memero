from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase, JSONField

db = SqliteExtDatabase('data.db')

class BaseModel(Model):
    class Meta:
        database = db

class Meme(BaseModel):
    filename =  TextField()
    tags = JSONField()

db.connect()
db.create_tables([Meme])
from peewee import *
import os
from playhouse.sqlite_ext import SqliteExtDatabase, JSONField

UPLOAD_FOLDER = '/app/data'
MEME_FOLDER = UPLOAD_FOLDER + '/memes'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(MEME_FOLDER )
    os.makedirs(UPLOAD_FOLDER + '/database')

db = SqliteExtDatabase(None)

class BaseModel(Model):
    class Meta:
        database = db

class Meme(BaseModel):
    filename = TextField()
    tags = JSONField()

db.init(database='./data/database/data.db')
db.connect()
db.create_tables([Meme])
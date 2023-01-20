from peewee import *
import os
from playhouse.sqlite_ext import SqliteExtDatabase, JSONField

UPLOAD_FOLDER = '/app/data'
MEME_FOLDER = UPLOAD_FOLDER + '/memes'
DB_FOLDER = UPLOAD_FOLDER + '/database'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(MEME_FOLDER):
    os.makedirs(MEME_FOLDER )
if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)

db = SqliteExtDatabase(None)

class BaseModel(Model):
    class Meta:
        database = db

class Meme(BaseModel):
    filename = TextField()
    tags = JSONField()

db.init(database='./data/database/data.db')
db.connect(reuse_if_open="sqlite:////data/database/data.db")
db.create_tables([Meme])
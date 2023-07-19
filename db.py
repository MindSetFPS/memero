from peewee import *
import os
from playhouse.sqlite_ext import SqliteExtDatabase, JSONField

UPLOAD_FOLDER = os.path.join(os.getcwd(), "data") 
MEME_FOLDER = os.path.join(UPLOAD_FOLDER, 'memes')
DB_FOLDER = os.path.join(UPLOAD_FOLDER, 'database') 

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    print("current working directory: ", os.getcwd())
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

db.init(database= os.path.join(DB_FOLDER,'data.db'))
db.connect(reuse_if_open="sqlite:////data/database/data.db")
db.create_tables([Meme])
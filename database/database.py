from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

import os

import threading
import asyncio

from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, UniqueConstraint, func


# if bool(os.environ.get("WEBHOOK", False)):
   # from sample_config import Config
# else:
  #  from config import Config
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", 12345))
API_HASH = os.environ.get("API_HASH")
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
DOWNLOAD_LOCATION = "./DOWNLOADS"
TG_MAX_FILE_SIZE = 2097152000
CHUNK_SIZE = 128
DB_URI = os.environ.get("DATABASE_URL", "")
BANNED_USERS = []


def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()

INSERTION_LOCK = threading.RLock()

class Thumbnail(BASE):
    __tablename__ = "thumbnail"
    id = Column(Integer, primary_key=True)
    msg_id = Column(Integer)
    
    def __init__(self, id, msg_id):
        self.id = id
        self.msg_id = msg_id

Thumbnail.__table__.create(checkfirst=True)

async def df_thumb(id, msg_id):
    with INSERTION_LOCK:
        msg = SESSION.query(Thumbnail).get(id)
        if not msg:
            msg = Thumbnail(id, msg_id)
            SESSION.add(msg)
            SESSION.flush()
        else:
            SESSION.delete(msg)
            file = Thumbnail(id, msg_id)
            SESSION.add(file)
        SESSION.commit()

async def del_thumb(id):
    with INSERTION_LOCK:
        msg = SESSION.query(Thumbnail).get(id)
        SESSION.delete(msg)
        SESSION.commit()

async def thumb(id):
    try:
        t = SESSION.query(Thumbnail).get(id)
        return t
    finally:
        SESSION.close()

import pyrogram
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", 12345))
API_HASH = os.environ.get("API_HASH")
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
DOWNLOAD_LOCATION = "./DOWNLOADS"
TG_MAX_FILE_SIZE = 2097152000
CHUNK_SIZE = 128
DB_URI = os.environ.get("DATABASE_URL", "")

#if bool(os.environ.get("WEBHOOK", False)):
   # from sample_config import Config
#else:
   # from config import Config
#from Config import DOWNLOAD_LOCATION, TG_BOT_TOKEN, APP_ID, API_HASH, AUTH_USERS
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "Rename Bot",
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    AUTH_USERS.add(680815375)
    app.run()

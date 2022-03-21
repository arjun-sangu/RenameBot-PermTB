import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
#else:
   # from config import Config
from Config import DOWNLOAD_LOCATION, TG_BOT_TOKEN, APP_ID, API_HASH, AUTH_USERS
import pyrogram
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

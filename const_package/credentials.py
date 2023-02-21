from typing import Optional

from dotenv import dotenv_values


config: Optional[dict] = None

BOT_TOKEN: Optional[str] = None
TOKEN: Optional[str] = None
TOKEN_V4: Optional[str] = None
DB_CONNECTION_STRING: Optional[str] = None


def load_env_config():
    global config, BOT_TOKEN, TOKEN, TOKEN_V4, DB_CONNECTION_STRING
    config = dotenv_values(".env")
    BOT_TOKEN = config['BOT_TOKEN']
    TOKEN = config['TOKEN']
    TOKEN_V4 = config['TOKEN_V4']
    DB_CONNECTION_STRING = config['DB_CONNECTION_STRING']

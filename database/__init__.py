from database.db import connect_to_database
from database.redis_helper import connect_to_redis


def initialize():
    connect_to_database()
    connect_to_redis()

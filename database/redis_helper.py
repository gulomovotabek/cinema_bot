from typing import Optional

from redis import Redis

from const_package import const


redis_client: Optional[Redis] = None


def connect_to_redis():
    global redis_client
    print("Connecting to Redis...")
    redis_client = Redis()
    print("Connected to Redis!")


def set_to_redis(_key, _value):
    redis_client.set(_key, _value)


def get_lang(_key):
    lang = get_from_redis(_key)
    if lang is not None:
        return str(lang)[2:-1]
    lang = const.EN
    set_to_redis(_key, lang)
    return lang


def get_from_redis(_key):
    return redis_client.get(_key)

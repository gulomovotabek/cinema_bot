import json
import requests

from const_package.const import ISO_LANG
from const_package.endpoints import UPCOMING_MOVIES_URL, SEARCH_MOVIES_URL


def get_upcoming_movies(lang: str):
    res = requests.get(f"{UPCOMING_MOVIES_URL}&language={ISO_LANG[lang]}")
    return return_response(res)


def search_movie(query: str, lang: str):
    query_url = f"{SEARCH_MOVIES_URL}&query={query}&language={ISO_LANG[lang]}"
    res = requests.get(query_url)
    return return_response(res)


def return_response(res: requests.Response):
    if res.status_code != 200:
        return None
    return json.loads(res.content)

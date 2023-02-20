from .credentials import TOKEN, TOKEN_V4


BASE_URL = "https://api.themoviedb.org/3/"

IMAGE_BASE_URL = "https://image.tmdb.org/t/p/"

UPCOMING_MOVIES_URL = f"{BASE_URL}movie/upcoming?api_key={TOKEN}"
SEARCH_MOVIES_URL = f"{BASE_URL}/search/movie?api_key={TOKEN}"

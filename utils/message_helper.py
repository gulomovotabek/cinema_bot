def make_upcoming_movies_message(upcoming_movies: list):
    message = "Upcoming Movies"
    for index, upcoming_movie in enumerate(upcoming_movies):
        message += f"\n\n{index + 1}. {upcoming_movie}"
    return message

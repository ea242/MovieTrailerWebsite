import webbrowser


class Movie():
    """
    This class provides a way to store movie related information.
    The constructor takes four arguments which contains detail of the Movie.
    movie_title - title of the Movie.
    movie_storyline - a description of the Movie.
    poster_image - URL for a poster image of the Movie.
    trailer_youtube - URL for a youtube trailer.
    There is one function called show_tailer() 
    which opens the URL in trailer_youtube_url.
    """

    # Ratings used for movies
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Constructor for the Movie class
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Functions to open web browser with provided url
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

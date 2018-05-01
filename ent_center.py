import media
import fresh_tomatoes

# Movie objects for website
good_will = media.Movie("Good Will Hunting",
                        "A smart Boston guy who tries to understand relationships",
                        "http://coolspotters.com/files/photos/369706/good-will-hunting-profile.jpg",
                        "https://www.youtube.com/watch?v=ReIJ1lbL-Q8")

forrest_gump = media.Movie("Forrest Gump",
                           "A simple minded guy that goes through life",
                           "https://image.tmdb.org/t/p/original/yE5d3BUhE8hCnkMUJOo1QDoOGNz.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

ben_button = media.Movie("The Curious Case of Benjamin Button",
                         "A old man who dies as a baby",
                         "https://images-na.ssl-images-amazon.com/images/I/71A8mO-OqBL._SY445_.jpg",
                         "https://www.youtube.com/watch?v=VqeqaweXBV0")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://vignette.wikia.nocookie.net/disney/images/8/80/Toy_Story_-_Poster.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://i.pinimg.com/originals/c3/2e/40/c32e40b633ff92a2d3048f5ce8570c90.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")


inception = media.Movie("Inception",
                        "A group of people in dreams within dreams",
                        "http://2.bp.blogspot.com/_Iau3R3yMIr4/TMBDGzcvwSI/AAAAAAAACbQ/77grl8TYdK4/s1600/inception1.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

# List of movies for
movies = [good_will,forrest_gump,ben_button,toy_story,avatar,inception]

# function from fresh_tomatoes to genereate webpage
fresh_tomatoes.open_movies_page(movies)

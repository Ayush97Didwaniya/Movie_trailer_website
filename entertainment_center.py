# import fresh_tomatoes to access the function open_movies_page()!!
# import media to access the class Movie!!
import fresh_tomatoes
import media


# sending attributes value in function  __init__  of class Movie!!
# we are creating each instances for each movie by movie name!!
# padmavati movie : movie title, storyline, poster, trailer
padmavati = media.Movie(
    "padmavati", "a story of queen padmini",
    "https://upload.wikimedia.org/wikipedia/en/4/47/Padmavati_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=X_5_BLt76c0"
    )

# toystory movie : movie title,storyline, poster, trailer
toystory = media.Movie(
    "toy story",
    "a story of and is toys that comes to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # N0QA
    "https://www.youtube.com/watch?v=4KPTXpQehio"
    )

# Avatar movie: movie title, storyline, poster, trailer
avatar = media.Movie(
    "avatar",
    "a marien on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/"
    "Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
    )

# Monions movie: movie title,storyline, poster, trailer
minions = media.Movie(
    "minions",
    "Minions hilariously imagines centuries in which the"
    "search for greatest villain they could find",
    "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",  # NOQA
    "www.youtube.com/watch?v=vATjQSarl8g"
    )

# Midnight in paris movie: movie title,storyline, poster, trailer
midnight_in_paris = media.Movie(
    "midnight in paris",
    "Going back in time to meet authors",
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=BYRWfS2s2v4"
    )

# ratatouille movie: movie title, storyline, poster, trailer
ratatouille = media.Movie(
    "Ratatouille",
    "A rat is a chef in paris",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=ALUmKa_mpik"
    )
hunger_games = media.Movie(
    "hunger games",
    "A really real reality show",
    "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
    "https://www.youtube.com/watch?v=4S9a5V9ODuY"
    )

# list of moives intances!!
movies = [
    padmavati,
    toystory,
    avatar,
    minions,
    midnight_in_paris,
    ratatouille,
    hunger_games
    ]

fresh_tomatoes.open_movies_page(movies)

"""
The file fresh_tomatoes.py contains the open_movies_page() function that
will take in your list of movies and generate an HTML file including
this content, producing a website to showcase your favorite movie

print(media.Movie.__doc__)
// this will print the documentation of Movie class which is
in media module !!
"""

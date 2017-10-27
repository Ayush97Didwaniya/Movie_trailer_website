import fresh_tomatoes                                        # import fresh_tomatoes to access the function open_movies_page()!!
import media                                                 # to access the class Movie!!
padmavati = media.Movie("padmavati",            # we are creating each instances for each movie by movie name!!       
                        "a story of queen padmini",
                        "https://upload.wikimedia.org/wikipedia/en/4/47/Padmavati_Poster.jpg",
                        "https://www.youtube.com/watch?v=X_5_BLt76c0")          #sending attributes value in function __init__ of class Movie for instance padmavati!!
toystory = media.Movie("toy story",
                       "a story of and is toys that comes to life",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=4KPTXpQehio")
avatar = media.Movie("avatar",
                     "a marien on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
minions = media.Movie("minions",
                      "Minions hilariously imagines centuries in which the little guys have sought to serve the greatest villain they could find, but quickly settles into more conventional cartoon territory.",
                      "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",
                      "www.youtube.com/watch?v=vATjQSarl8g")
midnight_in_paris = media.Movie("midnight in paris",
                                "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")
ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=ALUmKa_mpik")
hunger_games = media.Movie("hunger games",
                           "A really real reality show",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")
movies = [padmavati,toystory, avatar, minions, midnight_in_paris, ratatouille, hunger_games]    #list of moives intances !!
fresh_tomatoes.open_movies_page(movies)
"""
    The file fresh_tomatoes.py contains the open_movies_page() function that will take in your list of
    movies and generate an HTML file including this content, producing a website to showcase your favorite movies
"""
# print(media.Movie.__doc__)            // this will print the documentation of Movie class which is in media module !!

import webbrowser     #webbrowser module import to use function open
# we import webroser for open the youtubeurl
class Movie():
    """ this class provides a way to store movie related information """
    VALID_RATINGS = ["G","PG","PG-13","R"]        # VALID_RATINGS is class variable can access through each object
    def __init__(self,movie_title,movie_storyline,movie_image,youtube_trailer):     # self is referencing the instance
          self.title=movie_title                    # self.title mentioning instance variable taking value from attributes of function for each instance 
          self.storyline=movie_storyline            
          self.poster_image_url=movie_image         
          self.trailer_youtube_url=youtube_trailer
        
    def show_trailer(self):                         # class movie have show trailer method which is for open trailer of movie
          webbrowser.open(self.trailer_youtube_url)   # webbrowser.open() function use to open the url content of webpage
          

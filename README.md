# Movie_trailer_website
this will show movies posters which are statically added using python code. when we click on the poster it will show trailer of that movie.

## Example 
![screenshot of website](Capture.PNG)

## code files
#### media.py

* Having class variables title(for storing title of movie) , storyline(a short description about movie) , poster_image_url(link to the poster image) , trailer_youtube_url(link to the youtube trailer)

* Having a method show_trailer()(to open trailer in browser window)

#### entertainment_center.py

Objects for different movies are created and intialized using constructors.
## Steps to execute project
* install python
* clone the repository
* run fresh_tomatoes.html file

## To add more movies in page 

* open entertainment_center.py
* create a new object and intialize it using constructor e.g. movie_name = media.Movie(movie_title, movie_storyline, image_url, youtube_url)
* add the movie_name to movies list e.g. movies = [toy_story, avatar]
* run entertainment_center.py
* run index.html

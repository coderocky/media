import webbrowser

#Define class Movie and attributes. 
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #The show_trailer function will open a new browser window for the movie trailer.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url, new=2)

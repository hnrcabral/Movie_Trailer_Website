import webbrowser  # import webbrowser to open websites


class Movie():  # class Movie serves as a template for each instance within
                # entertainmentcenter.py file
    '''
    This class provides a way to store movie related information.
    self - the instance movie
    movie_title - the movie title
    movie_storyline - the plot of the movie
    poster_image - main coverphotoof the movie
    trailer_youtube - the Youtube link to the trailer of the movie
    '''

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):  # outlines the variables to be used
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

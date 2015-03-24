import webbrowser


class Movie():
    # Define a class to store movie information and display trailer
    def __init__(self, title, synopsis, poster_image_url, trailer_youtube_url):
        self.title = title
        self.synopsis = synopsis
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        # displays movie trailer
        webbrowser.open(self.trailerUrl)

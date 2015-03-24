from movies import Movie
import fresh_tomatoes

# Fallen Angels
fallen_angels = Movie("Fallen Angels",
                      "Two stories in Hong Kong with a few casual run-ins.",
                      "http://upload.wikimedia.org/wikipedia/en/0/04/Fallen-Angels-Poster.jpg",
                      "https://www.youtube.com/watch?v=-NfjlmxuCrU")

# Akira
akira = Movie("Akira",
              "Neo-Tokyo is about to explode.",
              "http://upload.wikimedia.org/wikipedia/en/5/5d/AKIRA_%281988_poster%29.jpg",
              "https://www.youtube.com/watch?v=-UhLderbuGI")

# Amelie
cityLostChildren = Movie("City of Lost Children",
                         "90s French Steampunk",
                         "http://upload.wikimedia.org/wikipedia/en/4/40/City_of_lost_children_french_movie_poster.jpg",
                         "https://www.youtube.com/watch?v=CNYG9cXTSds",)


# Run Lola Run
lolaRennt = Movie("Run Lola Run",
                  "A study of how small changes can create different outcomes",
                  "http://upload.wikimedia.org/wikipedia/en/f/f5/Lola_Rennt_poster.jpg",
                  "https://youtu.be/LbYk77LjDtQ")

# Night on earth
night_on_earth = Movie("Night On Earth",
                       "5 Stories, 5 Taxi Drivers, 5 Locations, One Night",
                       "http://upload.wikimedia.org/wikipedia/en/f/f9/Nightonearth.jpg",
                       "https://www.youtube.com/watch?v=XkKBbibm1FM")


movieList = [fallen_angels, akira, cityLostChildren, lolaRennt, night_on_earth]

fresh_tomatoes.open_movies_page(movieList)
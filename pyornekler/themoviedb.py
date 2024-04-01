import requests


class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.ogr/3"
        self.api_key = "ac13c261599f55a32e7a291336b9561d"

    def getPopulars(self):
        response = requests.get(
            f"{self.api_url}/movie/popular?api_key={self.api_key}language=en-US&page=1"
        )
        return response.json()


movieApi = theMovieDb()
while True:
    secim = input("1- Popular Movies\n2-Exit\nSeçim: ")
    if secim == "2":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            print(movies)

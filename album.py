class Album:
    def __init__(self,id,title,genre,artist,price,year):
        self.id = id
        self.title = title
        self.genre = genre
        self.artist_name = artist
        self.price = price
        self.release_year = year
        self.songs = []
    def __str__(self):
        return f"{self.id}  |  {self.title} | {self.artist_name}"
class Movie:
    def __init__(self, movieName, director, year, rating=None):
        self.movieName = movieName.upper()
        self.director = director.upper()
        self.year = year 
        self.rating = rating 

    def getMovieName(self):     
       return self.movieName

    def getDirector(self):
        return self.director

    def getYear(self):
        return self.year 

    def getRating(self):
        return self.rating 

    def getMovieDetails(self):
        parts = self.director.split(", ")
        if len(parts) == 2:
            name = parts[1] + " " + parts[0] 
        else:
            name = self.director 

        return "{} directed by {} ({}), Rating: {}".format(self.movieName, name, self.year, self.rating)    
    

    def _key(self):
        return (self.director, self.year, self.movieName) 

    def __gt__(self, other):
        return self._key() > other._key()

    def __lt__(self, other):
        return self._key() < other._key()

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False 
        return self._key() == other._key()
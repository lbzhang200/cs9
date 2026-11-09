from MovieCollectionNode import MovieCollectionNode


class MovieCollection:
    def __init__(self):
        self.head = None 

    def isEmpty(self):
        return self.head == None 

    def getNumberOfMovies(self):
        count = 0 
        current = self.head 
        while current != None: 
            count += 1
            current = current.getNext()
        return count 

    def insertMovie(self, movie):
        current = self.head 
        previous = None 
        stop = False 

        while current != None and not stop:
            if current.getData() > movie:
                stop = True 
            else:
                previous = current 
                current = current.getNext() 

        temp = MovieCollectionNode(movie)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp 

        else:
            temp.setNext(current)
            previous.setNext(temp)

    def getAllMoviesInCollection(self):
        output = ""
        current = self.head
        while current != None:
            output += current.getData().getMovieDetails() + "\n"
            current = current.getNext()
        return output 

    def getMoviesByDirector(self, director):
        director = director.upper()
        output = "" 
        current = self.head 
        while current != None: 
            if current.getData().getDirector() == director:
                output += current.getData().getMovieDetails() + "\n"
            current = current.getNext()
        return output 

    def removeDirector(self, director):
        director = director.upper()
 
        while self.head != None and self.head.getData().getDirector() == director:
            self.head = self.head.getNext()
 
        if self.head == None:
            return
 
        previous = self.head
        current = self.head.getNext()
        while current != None:
            if current.getData().getDirector() == director:
                previous.setNext(current.getNext())
            else:
                previous = current
            current = current.getNext()
 
    def avgDirectorRating(self, director):
        director = director.upper()
        total = 0
        count = 0
        current = self.head
        while current != None:
            movie = current.getData()
            if movie.getDirector() == director and movie.getRating() != None:
                total += movie.getRating()
                count += 1
            current = current.getNext()
        if count == 0:
            return None
        return round(total / count, 2)
 
    def recursiveSearchMovie(self, movieName, movieNode):
        if movieNode == None:
            return False
        if movieNode.getData().getMovieName() == movieName.upper():
            return True
        return self.recursiveSearchMovie(movieName, movieNode.getNext())
 
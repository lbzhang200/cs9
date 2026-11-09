from Movie import Movie
from MovieCollection import MovieCollection
from MovieCollectionNode import MovieCollectionNode


# ---------- Movie ----------
def test_movieConstructorAndGetters():
    m = Movie("The Godfather", "Coppola, Francis", 1972, 9.2)
    assert m.getMovieName() == "THE GODFATHER"
    assert m.getDirector() == "COPPOLA, FRANCIS"
    assert m.getYear() == 1972
    assert m.getRating() == 9.2


def test_movieDefaultRating():
    m = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968)
    assert m.getRating() == None


def test_getMovieDetails():
    m1 = Movie("The Godfather", "Darabont, Frank", 1972, 9.4)
    m2 = Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968)
    assert m1.getMovieDetails() == \
        "THE GODFATHER directed by FRANK DARABONT (1972), Rating: 9.4"
    assert m2.getMovieDetails() == \
        "2001: A SPACE ODYSSEY directed by STANLEY KUBRIC (1968), Rating: None"


def test_movieGreaterThan():
    a = Movie("Casablanca", "Curtiz, Michael", 1942)
    b = Movie("City Lights", "Chaplin, Charlie", 1931)
    c = Movie("Modern Times", "Chaplin, Charlie", 1936)
    d = Movie("Work", "Chaplin, Charlie", 1915)
    e = Movie("The Champion", "Chaplin, Charlie", 1915)
    assert a > b          # director
    assert c > b          # same director, year
    assert d > e          # same director + year, name
    assert not (b > a)
    assert not (b > b)


# ---------- MovieCollectionNode ----------
def test_nodeCreation():
    m = Movie("Casablanca", "Curtiz, Michael", 1942, 8.8)
    n = MovieCollectionNode(m)
    assert n.getData() == m
    assert n.getNext() == None


def test_nodeSetters():
    m1 = Movie("Casablanca", "Curtiz, Michael", 1942, 8.8)
    m2 = Movie("The Matrix", "Wachowski, Lana", 1999, 9.1)
    n1 = MovieCollectionNode(m1)
    n2 = MovieCollectionNode(m2)
    n1.setNext(n2)
    assert n1.getNext() == n2
    n1.setData(m2)
    assert n1.getData() == m2


# ---------- MovieCollection ----------
def makeCollection():
    mc = MovieCollection()
    mc.insertMovie(Movie("Casablanca", "Curtiz, Michael", 1942, 8.8))
    mc.insertMovie(Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2))
    mc.insertMovie(Movie("The Matrix", "Wachowski, Lana", 1999, 9.1))
    mc.insertMovie(Movie("Work", "Chaplin, Charlie", 1915, 6.2))
    mc.insertMovie(Movie("Modern Times", "Chaplin, Charlie", 1936, 8.9))
    mc.insertMovie(Movie("City Lights", "Chaplin, Charlie", 1931, 9.0))
    mc.insertMovie(Movie("The Champion", "Chaplin, Charlie", 1915, 6.7))
    return mc


def test_emptyCollection():
    mc = MovieCollection()
    assert mc.isEmpty() == True
    assert mc.head == None
    assert mc.getNumberOfMovies() == 0
    assert mc.getAllMoviesInCollection() == ""


def test_insertAndCount():
    mc = makeCollection()
    assert mc.isEmpty() == False
    assert mc.getNumberOfMovies() == 7


def test_getAllMoviesInCollection():
    mc = MovieCollection()
    mc.insertMovie(Movie("Casablanca", "Curtiz, Michael", 1942, 8.8))
    mc.insertMovie(Movie("2001: A Space Odyssey", "Kubric, Stanley", 1968, 9.2))
    mc.insertMovie(Movie("The Matrix", "Wachowski, Lana", 1999, 9.1))
    mc.insertMovie(Movie("Modern Times", "Chaplin, Charlie", 1936, 8.9))
    mc.insertMovie(Movie("City Lights", "Chaplin, Charlie", 1931, 9.0))
    assert mc.getAllMoviesInCollection() == \
        "CITY LIGHTS directed by CHARLIE CHAPLIN (1931), Rating: 9.0\n" \
        "MODERN TIMES directed by CHARLIE CHAPLIN (1936), Rating: 8.9\n" \
        "CASABLANCA directed by MICHAEL CURTIZ (1942), Rating: 8.8\n" \
        "2001: A SPACE ODYSSEY directed by STANLEY KUBRIC (1968), Rating: 9.2\n" \
        "THE MATRIX directed by LANA WACHOWSKI (1999), Rating: 9.1\n"


def test_insertFrontMiddleEnd():
    mc = MovieCollection()
    mc.insertMovie(Movie("B", "M, M", 2000))
    mc.insertMovie(Movie("A", "A, A", 2000))   # front
    mc.insertMovie(Movie("C", "Z, Z", 2000))   # end
    mc.insertMovie(Movie("D", "M, M", 1990))   # middle (year tiebreak)
    assert mc.head.getData().getMovieName() == "A"
    assert mc.getAllMoviesInCollection() == \
        "A directed by A A (2000), Rating: None\n" \
        "D directed by M M (1990), Rating: None\n" \
        "B directed by M M (2000), Rating: None\n" \
        "C directed by Z Z (2000), Rating: None\n"


def test_getMoviesByDirector():
    mc = makeCollection()
    expected = \
        "THE CHAMPION directed by CHARLIE CHAPLIN (1915), Rating: 6.7\n" \
        "WORK directed by CHARLIE CHAPLIN (1915), Rating: 6.2\n" \
        "CITY LIGHTS directed by CHARLIE CHAPLIN (1931), Rating: 9.0\n" \
        "MODERN TIMES directed by CHARLIE CHAPLIN (1936), Rating: 8.9\n"
    assert mc.getMoviesByDirector("Chaplin, Charlie") == expected
    assert mc.getMoviesByDirector("chaplin, CHARLIE") == expected
    assert mc.getMoviesByDirector("Nolan, Christopher") == ""


def test_removeDirectorMiddleAndFront():
    mc = makeCollection()
    mc.removeDirector("chaplin, charlie")   # front block
    assert mc.getNumberOfMovies() == 3
    assert mc.getMoviesByDirector("Chaplin, Charlie") == ""
    assert mc.head.getData().getMovieName() == "CASABLANCA"
    mc.removeDirector("Kubric, Stanley")    # middle
    assert mc.getNumberOfMovies() == 2
    mc.removeDirector("Wachowski, Lana")    # end
    assert mc.getNumberOfMovies() == 1
    mc.removeDirector("Nobody, Here")       # not present
    assert mc.getNumberOfMovies() == 1
    mc.removeDirector("Curtiz, Michael")    # last one
    assert mc.isEmpty() == True


def test_removeDirectorEmpty():
    mc = MovieCollection()
    mc.removeDirector("Chaplin, Charlie")
    assert mc.isEmpty() == True


def test_avgDirectorRating():
    mc = MovieCollection()
    mc.insertMovie(Movie("Casablanca", "Curtiz, Michael", 1942, 8.8))
    mc.insertMovie(Movie("Modern Times", "Chaplin, Charlie", 1936, 8.9))
    mc.insertMovie(Movie("The Matrix", "Wachowski, Lana", 1999, 9.1))
    mc.insertMovie(Movie("City Lights", "Chaplin, Charlie", 1931, 9.0))
    mc.insertMovie(Movie("Work", "Chaplin, Charlie", 1915))   # None ignored
    mc.insertMovie(Movie("Unrated", "Nolan, Chris", 2000))
    assert mc.avgDirectorRating("Chaplin, Charlie") == 8.95
    assert mc.avgDirectorRating("curtiz, michael") == 8.8
    assert mc.avgDirectorRating("Nolan, Chris") == None
    assert mc.avgDirectorRating("Nobody, Here") == None


def test_recursiveSearchMovie():
    mc = makeCollection()
    assert mc.recursiveSearchMovie("Modern times", mc.head) == True
    assert mc.recursiveSearchMovie("the matrix", mc.head) == True
    assert mc.recursiveSearchMovie("Inception", mc.head) == False
    empty = MovieCollection()
    assert empty.recursiveSearchMovie("Anything", empty.head) == False
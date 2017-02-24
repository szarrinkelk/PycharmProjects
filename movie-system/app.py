from movie import Movie
from user import User

user = User("Jose")

my_movie = Movie("The Matrix", "Sci-Fi", True)

user.movies.append(my_movie)

print(user.watched_movies())
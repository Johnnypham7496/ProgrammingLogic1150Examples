# a favorite movie list in reverse alphabetical order
# variable and list of movies
movies = ['Inception', 'Avengers Endgame', 'Avatar 2', 'Big Trouble in Little China']
# converting the movie variable to a reverse alphabetical list
favorite_movies = sorted(movies, reverse=True)
# for loop to list out the movies in different line
for movies in favorite_movies:
    print(movies)
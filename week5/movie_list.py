# a favorite movie list in reverse alphabetical order
# variable and list of movies
favorite_movies = ['Inception', 'Avengers Endgame', 'Avatar 2', 'Big Trouble in Little China']
# converting the movie variable to a reverse alphabetical list
favorite_movies = sorted(favorite_movies, reverse=True)
# for loop to list out the movies in different line
for movies in favorite_movies:
    print(movies)


# append() is how you add more items to a list but for some reason it's not working on my end
# movies.append('The Dark Knight')
# print(movies)

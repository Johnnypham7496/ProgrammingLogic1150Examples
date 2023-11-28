import secrets

artist_playlist = ['Tory Lanz', 'SZA', 'Treasure', 'B.I.', 'Jackson Wang', 'Tia', 'Joji', 'GEMINI']
# print(random.choice(playlist))
secrets.SystemRandom().shuffle(artist_playlist)
# print(playlist)
for number, artist in enumerate(artist_playlist):
    print(number, artist)

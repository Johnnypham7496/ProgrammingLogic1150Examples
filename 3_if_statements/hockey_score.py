"""
Hockey games

if the Minnesota Wild score 2
The Detroit Red Wings score 3

Who won?

Substitute your teams of your choice if preferred. Or baseball/basketball/soccer/other sport.

"""


minnesota_score = 2
detroit_score = 3


if detroit_score % 3 == 0:
    print('The score is a multiple of 3')

if minnesota_score > detroit_score:
    print('Minnesota wilds won!')
elif detroit_score > minnesota_score:
    print('Detroit Red Wings won!')

else:
    print('The game is tie - both teams have the same score')

print('That\'s then end of the program!')
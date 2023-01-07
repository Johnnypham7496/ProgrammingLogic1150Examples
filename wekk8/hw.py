# variable with string in triple quotes for text
text = """Yeah, front back side to side
Pull up, then I drop the top on a new ride
Bust down, Cartier cost thirty-five
Thirty thousand square feet in the air, stay fly
Red carpet, I was fresh suit and tie
Jumped off the stage, I don't even know why
Everytime I drop a new hit, we on fire
Yeah, we going viral, I know that I inspired you
Jump on a jet, let's get away
Out of town, find somewhere away
We can't be found, bust down that Cartier
I came from the ground, ain't no other man
In the town, rolling up the Zaza woods
Right out the pound
Don't look at my water, you gon' drown
Everybody know Big Draco, it's going down"""
list_of_special_characters = [",", "'", ""]
lyrics = text.lower()
for punctuation in list_of_special_characters:
    lyrics = lyrics.replace(punctuation, '')

lyric_words = lyrics.split()
print(f'Number of words in the song is {len(lyric_words)}')
lyric_line = lyrics.split('\n')
print(f'The number of lines in the lyric is {len(lyric_line)}')
# this is a for loop that runs through the entire code and determines how many 'unique' words are there
# this loop will exclude all duplicate words
# first needs to set the lyrics_word into a dictionary adn will go through the dictionary key by key
# continues to add unique words into the counter everytime the lyric_word code loops
duplicate_words = set(lyric_words)
dictionary_words = dict()
counter = 0
for word in duplicate_words:
    dictionary_words[word] = lyrics.count(word)
    if dictionary_words[word] == 1:
        counter = counter + 1
print(f'The number of unique words in the song are {counter}')

print()
for word in dictionary_words.keys():
    print(f'{word:<20}{len(word)}')


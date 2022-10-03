from random import randint
from secrets import choice

def word_random():
    letters = ["p", "a", "t", "o", "n"]
    index = randint(0, len(letters) -1)
    return letters[index]
    
for _ in range(0,5):
    word = word_random()
    print (word, end="")

    
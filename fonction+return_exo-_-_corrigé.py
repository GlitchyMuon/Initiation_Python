from random import randint


def word_random():
    letters = ["p", "a", "t", "o", "n"]
    index = randint(0, len(letters) -1)
    return letters[index]
    
for _ in range(5):
    word = word + word_random()

print (word)

    
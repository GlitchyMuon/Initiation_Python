from random import randint

def random_letter():

    possibilities = ["a", "b", "c", "d", "e"]
    index = randint(0, len(possibilities) - 1)
    return possibilities[index]



word = ""

for _ in range(5):
    word = word + random_letter()

print(word)
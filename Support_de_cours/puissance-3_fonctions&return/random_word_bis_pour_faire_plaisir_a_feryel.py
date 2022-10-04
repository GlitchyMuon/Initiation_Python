from random import randint

def random_letter():
    letters = ["a", "h", "k", "o", "n", "s", "t"]
    index = randint(0, len(letters) - 1)
    return letters[index]

def random_word(n):
    word = ""

    for _ in range(n):
        word = word + random_letter()
    
    return word

n_letters = input("Nombre de lettres: ")
n_letters = int(n_letters)

print(random_word(n_letters))
from random import randint

def random_word(n):
    word = ""
    letters = ["a", "h", "k", "o", "n", "s", "t"]

    for _ in range(n):
        index = randint(0, len(letters) - 1)
        word = word + letters[index]
    
    return word

n_letters = input("Nombre de lettres: ")
n_letters = int(n_letters)

print(random_word(n_letters))
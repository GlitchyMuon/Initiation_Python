from random import randint

def random_word(len_word, letters):

    # protection contre les mots trop grands (car on a que 8 letters disponibles)
    if len_word > len(letters):
        len_word = len(letters)

    word = ""

    for _ in range(len_word):
        index = randint(0, len(letters) - 1)
        letter = letters.pop(index)
        word += letter

    return word


# --- main ---

print(random_word(3, ["p", "y", "t", "h", "o", "n"]))
print(random_word(5,["b", "o", "a", "r", "d"]))
print(random_word(10, ["c", "u", "p"]))

from random import randint

def random_word(len_word):
    letters = ["a", "i", "l", "n", "o","r", "s", "t"]
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

print(random_word(3))
print(random_word(5))
print(random_word(10))

from random import randint

def random_word():
    letters = ["a", "i", "l", "n", "o","r", "s", "t"]
    word = ""

    for _ in range(5):
        index = randint(0, len(letters) - 1)
        letter = letters.pop(index)
        word += letter

    return word


# --- main ---

print(random_word())
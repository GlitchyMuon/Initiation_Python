from random import randint

def n_letter_word(len_word):
    letters = ["a", "i", "l", "n", "o", "r", "s", "t"]
    
    index = randint(0, len(letters)-1)
    word = []
    count = 0
    if letters[index] == index :
        count += 1
        word.append(letters[index])
    return word

print(n_letter_word(5))





    
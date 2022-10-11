from random import randint

def random_word(len_word, letters):
    letters = ["a", 
"i", "l", "n", "o", "r", "s", "t"]
    # protection contre les mots trop grand (car on n'a que 8 lettresn disponibles)
    if len_word > len(letters) :
        len_word = len(letters)
    
    word = ""
    
    for _ in range(5) :
          index = randint(0, len(letters)-1)
          letter = letters.pop(index) # il fait sauter la lettre à l'index à chaque fois
          word += letter
    return word

## --- main

print(random_word(3, ["p", "y", "t", "h", "o", "n"])) #pas oublier la double parenthèse fermante. ET pas metttre l'argument entre deux parenthèses !
print(random_word(5, ["b", "o", "a", "r", "d"]))
print(random_word(10, ["c", "u", "p"]))
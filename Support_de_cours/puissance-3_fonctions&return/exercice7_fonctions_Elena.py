# Ecrivez une fonction qui écrit un mot de 5 lettres avec les lettres suivantes: "a", "i", "l", "n", "o", "r", "s", "t". 
# Le mot sera ensuite retourné par la fonction. Attention les lettres ne peuvent être utilisées qu'une seule fois dans le mot.
# Par exemple: "tsoni" est un mot valide mais pas "liara"

from random import randint

def word_creator(word_len):
    letters = ["a", "i", "l", "n", "o", "r", "s", "t"]
    word = ""
    while len(word) < word_len:
        index = randint(0, len(letters)-1)
        letter = letters[index]
        if letter not in word:  # condition que les lettres ne soient utilisées qu'une seule fois
            word += letter
    return word

print(word_creator(7))


# Exercice 7-bis
# Changer la fonction précédente en lui ajoutant un argument qui représentera le nombre de lettre du mot. 
# Changer le code de la fonction pour que le nombre de lettre du mot généré ne soit plus 5, mais le nombre passé en paramètre.
# OK, fait!

# Exercice 7-tris
# Changer encore la fonction précédente en lui ajoutant un autre argument qui représentera cette fois une liste de lettres 
# autorisées. Changer le code de la fonction pour que la liste passée en paramètre soit utilisée à la place de celle déclarée 
# dans la fonction.

def word_creator(word_len, letters):
    word = ""
    while len(word) < word_len:
        index = randint(0, len(letters)-1)
        letter = letters[index]
        if letter not in word:
            word += letter
    return word

print(word_creator(7, ["a", "e", "m", "p", "r", "s", "t", "u", "y"]))
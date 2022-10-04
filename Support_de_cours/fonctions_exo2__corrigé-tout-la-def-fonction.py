#Créez une fonction qui prendra en paramètre un nombre de lettres désiré et qui 
#renverra un mot de la longueur correspondante composé de lettres prises au 
#hasard parmis "a", "h", "k", "o", "n", "s" et "t".
#Le programme principal demandera à l'utilisateur combien de lettres il veut dans 
#son mot et affichera ensuite un mot fabriqué par la fonction

from random import randint

def random_word():
    letters = ["a", "h", "k", "o", "n", "s", "t"]
    index = randint(0, len(letters) -1)
    
    
  
    for _ in range(n):
        index = randint(0, len(letters) - 1)
        word = word + letters[index]
    
    return word

n_letters = input("Nombre de lettres: ")
n_letters = int(n_letters)

print(random_word(n_letters))
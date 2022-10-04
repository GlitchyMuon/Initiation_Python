#Créez une fonction qui prendra en paramètre un nombre de lettres désiré et qui 
#renverra un mot de la longueur correspondante composé de lettres prises au 
#hasard parmis "a", "h", "k", "o", "n", "s" et "t".
#Le programme principal demandera à l'utilisateur combien de lettres il veut dans 
#son mot et affichera ensuite un mot fabriqué par la fonction

from random import randint

def random_letter():
    letters = ["a", "h", "k", "o", "n", "s", "t"]
    index = randint(0, len(letters) -1)
    return letters[index]



def random_word(n):
    word = ""

    for _ in range(n) :
        word = word + random_letter()

    return word #important de mettre dans la def et pas dans la boucle for !! Sinon ça ne s'ajoute pas dans le word !

user_number = input("Combien de lettres : ")
user_number = int(user_number) #mettre ici car sinon dans le print, user_number n'est pas défini, s'il est dans la boucle

print(random_word(user_number))


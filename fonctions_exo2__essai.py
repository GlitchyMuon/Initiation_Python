#Créez une fonction qui prendra en paramètre un nombre de lettres désiré et qui 
#renverra un mot de la longueur correspondante composé de lettres prises au 
#hasard parmis "a", "h", "k", "o", "n", "s" et "t".
#Le programme principal demandera à l'utilisateur combien de lettres il veut dans 
#son mot et affichera ensuite un mot fabriqué par la fonction

from random import randint

def random_letter(index): #pas besoin de définir si juste après il est écrasé
    letters = ["a", "h", "k", "o", "n", "s", "t"]
    index = randint(0, len(letters) -1)
    return  letters[index]


word = ""
user_number = input("Combien de lettres : ")
user_number = int(user_number)


for _ in range(user_number) :
    word = word + random_letter(range(user_number))
    
print(word)

#Programme fonctionne ! Yay ! mais pas ce qui est demandé
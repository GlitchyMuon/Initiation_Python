# 1 - Générer un nombre aléatoire entre 1 et 10
from random import randint
d10 = randint(1, 10)
# 2 - Demander un nombre à l'utilisateur
number=input("Donne un nombre entre 1 et 10 : ")
print(number)
number = int(number)
# 3 - Comparer les nombres
if number == d10:
    print("Le nombre est égal au nombre à deviner. Vous avez gagné !")
elif number < d10:
    print("Le nombre est inférieur au nombre à deviner. Réessayez !")
else:
    print("Le nombre est supérieur au nombre à deviner. Réessayez !")



from random import randint
solution = randint(1, 10)

answer = None
while answer != solution :
    answer= input("Donne un nombre entre 1 et 10 :")
    answer=int(answer)

    if answer == solution:
        print("Le nombre est égal au nombre à deviner. Vous avez gagné !")
    elif answer < solution:
        print("Le nombre est inférieur au nombre à deviner. Réessayez !")
    else:
        print("Le nombre est supérieur au nombre à deviner. Réessayez !")

from random import randint
solution = randint(1, 10)

answer = None

essais = 3


while answer != solution and essais != 0 :
    answer= input("Donne un nombre entre 1 et 10, tu as " + str(essais) + " essais au total: ")
    answer=int(answer)
    essais = essais - 1
    
    if answer == solution:
        print("Bravo, tu as trouvé !")
       
    elif answer < solution:
        print("Le nombre est inférieur au nombre à deviner. Réessayes !")
        print("Tu as encore "+ str(essais) +" essais.")
    else:
        print("Le nombre est supérieur au nombre à deviner. Réessayes !")
        print("Tu as encore "+ str(essais) +" essais.")
if essais == 0 and answer != solution:
    print("Perdu ! Désolé tu as épuisé les 3 essais sans trouver la solution.")
    print("La solution était "+ str(solution) + ".")

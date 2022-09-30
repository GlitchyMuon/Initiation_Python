number = input("Entre un nombre (appuie sur 0 pour arrêter): ")
number = int(number)

greater = number
lower = number

# comparer le premier chiffre entré avec la suivante donnée, s'il est plus petit : afficher s'il est plus grand : afficher
while number != 0 :
    number = input("Entre un nombre (appuie sur 0 pour arrêter): ")
    number = int(number)
# Ici si on met : if number != 0:       il va ignorer le zéro.
    if greater < number :
        greater = number
    
    elif lower > number :
        lower = number

#si l'utilisateur met un chiffre négatif, le prog va en effet ignorer le zéro

print("Plus grand: " + str(greater) + ", plus petit: " + str(lower) + ".")
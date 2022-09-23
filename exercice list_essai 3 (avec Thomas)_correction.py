elements = [2, 3, 5, 7 ,11, 13]

index = input("Donne moi un nombre entre 0 et " + str(len(elements) - 1) + " :")
index = int(index)
while elements < 0 or elements >= len(elements) :

    print(elements)
print(elements [:index]) #pas besoin de préciser 0 ni la fin de la liste car il va d'office jusqu'à la limite de la liste
print(elements[index:])
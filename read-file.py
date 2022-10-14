groceries_file = open(r"data/groceries.txt") #(r"") permet d'indiquer à Python que c'est un chemin de fichier
groceries_list = groceries_file.read() #si on met un nombre comme 10 en paramètre, il va afficher les premiers caractères
groceries_file.close()

print(groceries_list)


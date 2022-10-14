groceries_file = open(r"data/groceries.txt") #(r"") permet d'indiquer à Python que c'est un chemin de fichier

data = groceries_file.readline() #si on met un nombre comme 10 en paramètre, il va afficher les premiers caractères

while data != "":
    if data[-1] == "\n":
        data = data[:-1]        #pour enlever le retour à la ligne du texte, plus le retour à la ligne du print
    print("- " + data)
    data = groceries_file.readline() # il lit et stocke ligne par ligne avec readline. L'importance d'écrire cette ligne de code car il prendra une nouvelle ligne (la suite)

groceries_file.close()




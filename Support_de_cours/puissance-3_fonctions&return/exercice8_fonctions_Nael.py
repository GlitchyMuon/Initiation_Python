#Écrivez une fonction qui prend une liste et un caractère comme arguments.La fonction va placer le caractère dans la dernière "case" (celle avec l'index le plus grand) de la liste qui est rempli par un ".".Après coup la fonction retournera la liste.Dans votre programme principal, utilisez la fonction pour remplir une liste remplie avec 6 ".". Faites donc  en sorte d'exécuter la fonction tant que la liste n'est pas remplie. Après chaque exécution de la fonction, affichez la liste.

#---fonctions

def remplissage (liste, caractere):
    for index in range (-1,-len(liste) -1, -1):
        if liste[index] == ".":
            liste[index] = caractere
            print (liste)
            return liste

#---main
pendu1 = ["a", "b", "c", ".", "e"]
pendu2 = [".", ".", ".", ".", "."]
pendu3 = ["a", ".", "c", "d", "."]

#for loop here avec le remplissage(pendu2,lettre)
while "." in pendu2:
    lettre = input("Lettre : ")
    remplissage(pendu2, lettre)


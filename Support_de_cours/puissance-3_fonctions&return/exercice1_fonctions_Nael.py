# Créer une fonction qui prend un mot argument et qui renvoie le mot inversé.Dans le programme principale, demandé à l'utilisateur de saisir un mot au clavier et affiché le mot inverse.Exemple:Si le mot est "hologramme" le mot affiché en retour sera "emmargoloh"

def mot_inverse(mot):
    inverse = ""
    for index in range(1, len(mot)+1): #je peux aussi faire avec for i in mot:
        lettre = mot[- index]
        inverse += lettre
    return inverse

word = input("Mot: ")
print(mot_inverse(word))   

user_input = input("Entrez le mot de passe : ")
mdp = "Pyth0n"
essais = 3 #si on veut faire comme dans guess the number, il faut faire user_input = None. Sinon ça crame une fois avant de rentrer dans le boucle et je devrais faire essais=2 et  essais != 0. Ici je dois mettre essais != 1 avec 3 essais.

while user_input != mdp and essais != 1 :
    user_input = input("Entrez le mot de passe : ")  
    essais = essais - 1
    if  user_input == mdp :
        print("Mot de passe valide.")

if essais >= 1 and user_input != mdp:
    print("Mot de passe incorrect.")

from random import randint

letters = ["a", "b", "c", "d", "e", "f"]
code = []
code_length = 4
essais = 3 #Mieux de mettre là ici car les variables sont toutes visibles ici (données meta), c'est plus clair. Sinon, c'est du moment qu'elle soit affectée Avant qu'elle soit utilisée dans la boucle

for _ in range(code_length):
   
    index = randint(0, len(letters) - 1)
    code.append(letters[index])
   


user_sequence = None #ou liste vide []


while user_sequence != code and essais > 0 : #mieux de mettre ">" même "!=" ça marche ici, mais pas dans d'autres cas si ça arrive au négatif, on sera bloqué dans le négatif ! En plus, la logique est :"je continue tant que" et pas "je m'arrête, quand"

    user_sequence = input("Proposez une séquence de code de " + str(code_length) +" lettres (sans espace): ") #même dans la proposition, bien d'utiliser len(code_length)
    print("Vous avez encore "+ str(essais) +" essais.")
   

    while len(user_sequence) != code_length :
        print("Vous avez encore "+ str(essais) +" essais.")
        user_sequence = input("Votre proposition doit contenir "  + str(code_length) +" lettres (sans espace) : ")

        if len(user_sequence) < code_length :
            print("Séquence pas assez longue.")
        elif len(user_sequence) == code_length :
            print("Proposition validée !")

    essais = essais - 1

    if essais == 0 and user_sequence != code :
        print("Perdu ! Désolé tu as épuisé les " + str(essais) + " essais sans trouver la solution.")
        print("La solution était "+ str(list(code)) + ".")

# Attention, à partir d'ici, il doit être dans le 1er while, pas indenté dans la 2ème while !!!

    user_sequence=list(user_sequence) 
    #très important de faire list de la séquence de proposition !

    print("Votre proposition (" + str(essais) + " restants)" + ": " + str(list(user_sequence))) #très important de faire list de la séquence de proposition !

    correct = []

    for n in range(code_length): #pas la liste(user_sequence) car string pas int, la variable n

        if user_sequence[n] == code[n]:
            correct.append(n)

    print(correct)
    

  # lettres bonnes mais pas à la bonne place
    misplaced = []

    for n in range(len(user_sequence)): # ou range(len(code_length)):
        for c in range(len(code)):
            if user_sequence[n]== code[c]:
                if c not in correct and c not in misplaced: #est-ce que j'ai pas déjà déterminé que cette lettre n'a pas déjà été égal et s'il n'a pas déjà été placé dans misplaced
                    if n not in correct :
                        misplaced.append(c)
                        break

    print("Il y a "+ str(len(correct)) + " lettre(s) correctes et bien placées, et " + str(len(misplaced)) + " correcte(s) mais mal placées.")

if code == user_sequence :
    print("Bravo ! Vous avez bien deviné !")
else :
    print("Dommage, La bonne réponse était :" + str(code))


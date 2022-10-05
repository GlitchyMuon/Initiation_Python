from random import randint

letters = ["a", "b", "c", "d", "e", "f"]
code = []
code_length = 4
essais = 12


for _ in range(code_length):
   
    index = randint(0, len(letters) - 1)
    code.append(letters[index])
   
#print(code)

user_sequence = None #ou liste vide []

while user_sequence != code and essais > 0:
    print("Nombre d'essai: " + str(essais))
    user_sequence = input("Proposez une séquence de code de " + str(code_length) +" lettres (sans espace) : ") #même dans la proposition, bien d'utiliser len(code_length)

    while len(user_sequence) != code_length :
        print("Nombre d'essai: " + str(essais))
        user_sequence = input("Votre proposition doit contenir "  + str(code_length) +" lettres (sans espace) : ")
    
        if len(user_sequence) < code_length :
            print("Séquence pas assez longue.")
        elif len(user_sequence) == code_length :
            print("Proposition validée !")
    
    essais = essais - 1

# Attention, à partir d'ici, il doit être dans le 1er while, pas indenté dans la 2ème while !!!

    user_sequence=list(user_sequence) #très important de faire list de la séquence de proposition !

    correct = []

    for n in range(code_length): #pas la liste(user_sequence) car string pas int, la variable n

        if user_sequence[n] == code[n]:
            correct.append(n)

    # lettres bonnes mais pas à la bonne place
    misplaced = []
    for n in range(code_length):
        for c in range(code_length):
            if user_sequence[n] == code[c]:
                if c not in correct and c not in misplaced:
                    if n not in correct:
                        misplaced.append(c)
                        break

    print("Lettres bien placées: " + str(len(correct)))
    print("Lettres mal placées: " + str(len(misplaced)))

if code == user_sequence:
    print("Bravo tu as bien deviné")
else:
    print("Dommage. La bonne réponse était: " + str(code))


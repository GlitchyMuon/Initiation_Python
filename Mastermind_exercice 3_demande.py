from random import randint

letters = ["a", "b", "c", "d", "e", "f"]
code = []
code_length = 4


for _ in range(code_length):
   
    index = randint(0, len(letters) - 1)
    code.append(letters[index])
   


user_sequence = input("Proposez une séquence de code de " + str(code_length) +" lettres (sans espace) : ") #même dans la proposition, bien d'utiliser len(code_length)

while len(user_sequence) != code_length :
    user_sequence = input("Votre proposition doit contenir "  + str(code_length) +" lettres (sans espace) : ")

    if len(user_sequence) < code_length :
        print("Séquence pas assez longue.")
    elif len(user_sequence) == code_length :
        print("Proposition validée !")

print(list(user_sequence))
from random import randint
answer = input("Ecrit un nombre : ")
answer = int(answer)
number  = randint(1, 20)
print(str(number) + " + " + str(answer) + " = " + str(number + answer))

from random import randint
answer = int(input("Ecrit un nombre : "))

while answer < 1 or answer > 5:
    answer = int(input("Ecrit un nombre : "))

number = randint(1, 5)

print(str(number) + " (" + str(answer - number) + ") ")

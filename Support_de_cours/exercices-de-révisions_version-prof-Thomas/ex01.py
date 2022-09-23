from random import randint

user = input("Nombre: ")
user = int(user)

rnd = randint(1, 20)

print(str(rnd) + " + " + str(user) + " = " + str(user + rnd))
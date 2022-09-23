from random import randint

user = input("Nombre: ")
user = int(user)

rnd = randint(1, 20)

if user >= rnd:
    print("success " + str(rnd))
else:
    print("failure " + str(rnd))
from random import randint

user = input("Nombre [1;5]: ")
user = int(user)

while user < 1 or user > 5:
    user = input("Nombre [1;5]: ")
    user = int(user)

rnd = randint(1, 5)

print(str(rnd) + " (" + str(rnd - user) + ") ")
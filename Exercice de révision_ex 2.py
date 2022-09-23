from random import randint
answer = input("Ecrit un nombre : ")
answer = int(answer)
number = randint(1, 20)
if answer >= number :
    print("success " + str(number))
else: 
    print("failure " + str(number))
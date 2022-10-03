from random import randint

def words():

    lang = randint(1,4)

    match lang:

        case 1:

            print("Bonjour")

        case 2:

            print("Hello")

        case 3:

            print("Ola")

        case 4:

            print("Ciao")



for i in range(1,100):

    words()
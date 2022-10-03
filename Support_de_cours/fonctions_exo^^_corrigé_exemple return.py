from random import randint

def say_random_hello():
    possibilities = ["Bonjour", "Hello", "Ola", "Ciao"]
    index = randint(0, len(possibilities) -1)

    return possibilities[index]

# -- Main --

for _ in range(100) :
    greetings = say_random_hello()
    print(greetings)
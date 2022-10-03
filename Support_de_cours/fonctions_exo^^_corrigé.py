from random import randint

def say_random_hello():
    possibilities = ["Bonjour", "Hello", "Ola", "Ciao"]
    index = randint(0, len(possibilities) -1)

    print(possibilities[index])

# -- Main --

for _ in range(100) :
    say_random_hello()
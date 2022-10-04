from random import randint

def say_random_hello():
    possibilities = ["Hello", "Ola", "Ciao", "Bonjour", "Dobry Den", "Konnichiwa "]
    index = randint(0, len(possibilities) -1)

    return possibilities[index]

# -- Main --

for _ in range(100):
    g = say_random_hello() + " Thomas"
    print(g, end=" ")
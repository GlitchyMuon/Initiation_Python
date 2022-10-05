from random import randint

def n_list(n):
    list = []
    for _ in range(n): #l'étendue de n, qu'on va définir dans le programme appelant
        list.append(randint(1, 6))
    return list #valeur de retour

print(n_list(10))
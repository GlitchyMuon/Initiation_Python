from random import randint

def random_card():
    card = ""
    card_list = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
    index = randint(0, len(card_list)-1)
    
    return card_list[index] # j'appelle l'élément à l'index de cette liste ! L'erreur que j'ai faite c'est de mettre l'élément dans une liste.

def random_cardlist(n):
    cardslist = [] # il faut absolument crée une liste ici, je ne peux pas utiliser random_cardlist() car sinon erreur de récursion car j'appelle ma fonction dans la même fonction def.
    while len(cardslist) < n :
    
        cardslist.append(random_card())
    return cardslist

# --- main

print(random_card())
print(random_cardlist(5))
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


def pokercards(cards):

    l = random_cardlist(10)
    max_count = 0 # la plus grande occurence
    for card in cards: # prend la valeur, pas l'index
        n = 0   # le nombre de fois qu'il apparaît
        for other in cards:
            if other == card: # ça compare un élément de la liste à tous les autres éléments et dès qu'il en rencontre un qui est le même, il rajoute le compte
                n += 1
            if max_count < n:   #si max_count est plus petit que n, max_count devient n (highscore)
                    max_count = n
        
        
    if max_count >= 5:
        print("Poker")
    elif max_count >= 4:
        print ("Carré")
    elif max_count >= 3:
        print("Brelan")
    elif max_count >= 2:
        print("Paire")
    else :
        print("Rien")
        
    return max_count
  

# --- main


#erreur de print(random_cardlist(10)) !!! pas print ceci car sinon c'est une Autre liste
var = random_cardlist(10)
print(var)
print(pokercards(var)) #
#erreur car si je print(pokercards(["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"])) !!! Et ça, ça imprime une liste Non-random car liste définie ! Oui c'est là qu'il faut mettre un argument, mais faut faire print(pokercars(random_cardlist(10)))
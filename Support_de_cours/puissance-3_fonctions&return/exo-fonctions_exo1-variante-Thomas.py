def reverse_word(word) :
    
    r_word = ""
    
    for index in range(-1, -len(word)-1, -1):
    #  commence à la fin du mot, se termine au début de la longueur négative du mot -1, et on décroit d'une lettre le pas
    
        r_word = r_word + word[index]
        
    return word
    # variante : return word[::-1] ou 
    # ça veut dire : du début à la fin à l'envers, en slicing, dans la direction omise <-
    
    w = input("Donne moi un mot: ")
    print("Mot inverse: " + reverse_word(w))
from random import randint

def word_creator(word_len):
    letters = ["a", "i", "l", "n", "o", "r", "s", "t"]
    word = ""
    while len(word) < word_len : # tant que la longueur de word est plus petit que l'argument word_len, qui est 5 dans l'exercice. On continue.
        index = randint(0, len(letters)-1)
        letter = letters[index]
        
        if letter not in word :
            word += letter #si la lettre n'est pas dans word, on rajoute à word =""
    return word #important de le mettre dans la boucle while, PAS dans le if !
    
print(word_creator(5))
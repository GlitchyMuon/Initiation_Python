#Écrivez une fonction qui prend un mot en paramètre et qui retourne ce même mot, mais sans les voyelles ("a", "e", "i", "o", "u", "y").Exemple: Si je passe "telegramme" comme paramètre, la fonction retournera"tlgrmm"
# 
# TO SOLVE : Attention: on ne gère pas les caractères spéciaux ! (erreur si on en met ou quel est la consigne?)
#ord() me rend le charactere asci d'une lettre

#Functions
def delete_vowels(word):
    vowels = ["a", "e", "i", "o", "u", "y"]
    without_vowels = ""
    for letter in word:
        if letter not in vowels: 
            without_vowels += letter
        
    return without_vowels

#main
input_word = input("Word : ")
print(delete_vowels(input_word))

#BONUS avec les ASCII numbers: elif (ord(lettre) >= 65 or ord(lettre) <= 90) and (ord(lettre) >= 97 or ord(lettre) =< 122)

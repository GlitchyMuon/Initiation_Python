def last_chara_place(char_list, character) :
    index = -1
    while char_list[index] != "." :
        index -= 1 # index = index -1 ou += -1
       
    char_list[index] = character   
    return char_list
    
def fill_list(array, character) :
    index = -1
    while array[index] != "." :
        index -= 1
        if (index < -len(array)): #si j'ai dépassé moins la longueur de la liste (= le début de mon tableau, ou le dernier élément à l'envers) : on retourne la liste sinon erreur. Sinon on peut faire zéro/0 au lieu de -len(array)
            return array
    array[index] = character # on remplace l'élément à cet index par le caractère.
    return array


 # --- Main
dot_list = ['.'] * 6 # synonyme. Mais en C : un caractère seul est entre ''. Une chaine de caractères est entre ""


for _ in range(len(dot_list)):
    dot_list = fill_list(dot_list, "X")
    print(dot_list)
# print(last_chara_place([".", ".", ".", ".", ".", "."], "?"))
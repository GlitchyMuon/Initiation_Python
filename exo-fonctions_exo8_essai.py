def last_chara_place(char_list, character) :
    index = -1
    while char_list[index] != "." :
        index -= 1 # index = index -1 ou += -1
       
    char_list[index] = character   
    return char_list
    


 # --- Main
print(last_chara_place([".", ".", ".", ".", ".", "."], "?"))
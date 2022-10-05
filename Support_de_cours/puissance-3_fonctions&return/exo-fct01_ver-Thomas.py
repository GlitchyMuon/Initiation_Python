def reverse_word(word):

    r_word = ""

    for index in range(-1, -len(word)-1, -1):
        r_word = r_word + word[index]
    return r_word

# -- main ---

w = input("Donne moi un mot: ")
print("Mot inverse: " + reverse_word(w)) 


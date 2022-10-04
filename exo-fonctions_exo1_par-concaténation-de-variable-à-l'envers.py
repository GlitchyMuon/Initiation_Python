def reverse_word(word):    
    r_word= ""
    
    for letter in word :
        r_word = letter + r_word
        print(r_word)

    return r_word

word = input("Entre un mot : ")

print(reverse_word(word))
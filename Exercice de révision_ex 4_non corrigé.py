word = input("Entre un mot au clavier : ")

words = [] #interchangé les deux lignes ci-dessus

while word != "stop" :
    if word[0] == "p":
        words.append(word)
    word = input("Entre un mot au clavier : ") #ne pas indenter cette ligne sinon il s'arrête et ne redemande pas

print(words)

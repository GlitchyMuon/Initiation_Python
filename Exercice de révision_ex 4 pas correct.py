words = []

word = input("Entre un mot au clavier : ")

while word != "stop" :
    words.append(word) # empêche de boucler à l'infini
    if word[0] == "p":
        words.append(word)
        word = input("Entre un mot au clavier : ")

print(words)

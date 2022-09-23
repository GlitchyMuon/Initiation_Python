words = []

word = input("Entre un mot au clavier :")
while word != "stop" :
    index=int(input("A quel index veux-tu placer le mot ? "))
    words.insert(index, word)
    word = input("Entre un mot au clavier :")
print(words)
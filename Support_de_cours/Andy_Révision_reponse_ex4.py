maList = []
word = None

while word != "stop":
    word = input("Enter a word 'stop to finish' : ")
    
    if word[0] == "p" :
        maList.insert(0,word)

print(maList)

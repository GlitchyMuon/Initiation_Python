elements = []

answer = input("Entre un mot au clavier :")
while answer != "stop" :
    elements.append(answer) # ↑ ligne montée. Pas oublier de stocker d'abord !
    answer = input("Entre un mot au clavier :")
print(elements)
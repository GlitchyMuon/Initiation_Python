elements = []

answer = input("Tapez ce que vous voulez : ")
elements.append(answer)
s = ""
for c in elements: #pour cette variable c qui n'est pas définie, je rajoute chacun des éléments sui suit
    s = s + c + ", " #s devient chaque fois le reste des ajouts
s= s[:-2]
print("Saisie au clavier: " + s)
elements = []

answer = input("Tapez ce que vous voulez : ")
elements.append(answer)
s = ""
for c in elements: #pour cette variable c qui n'est pas définie, je rajoute chacun des éléments qui suit
# je peux mettre answer et il va afficher simplement l'answer
    s=s+c+", " #s devient chaque fois la réponse answer
#on a rajouté l'expression ici pour afficher la réponse avec des ", ". Et je sais pas pourquoi, on a voulu ajouter l'expression en dehors de la boucle s=s[:-2] pour ne pas afficher ", " alors qu'en affichant simplement answer, tout aurait été plus simple
print("Saisie au clavier: " + s)
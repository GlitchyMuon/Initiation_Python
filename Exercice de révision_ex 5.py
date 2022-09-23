
list1 = [2, 3, 5, 7, 11, 13, 17, 23]
list2 = []
print(list1)
while len(list1) != 0: #> ou != car une liste peut jamais être en négatif
    removed=list1.pop(-1) #par défaut le pop si pas précisé, prend le dernier, donc on peut laiser vide
    list2.append(removed) #si on veut pas définir de variable : removed.append(list1.pop(-1)) en une ligne au lieu de deux
print(list1)    
print(list2) #si je mets print(list2) dans la boucle, il va afficher à chaque fois l'élément enlevé et ajouté

    

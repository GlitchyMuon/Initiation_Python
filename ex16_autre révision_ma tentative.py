#Quand on utilise la boucle for, on peut parcourir une collection par élément de la collection. Par exemple, si j'ai une liste < l = [4, 6, 8, 16] > et que je fais < for n in l: >, ça va créer une boucle qui va parcourir les 4 chiffres, une boucle qui passe 4 fois. < m = test, for c in m > va venir faire passer successivement "t" "e" "s" "t" car les éléments de ma collection sont des lettres. Deuxième chose, si on a un ensemble de valeurs comme le <l> du dessus et que je veux tester qu'une valeur se trouve dedans, j'écris < 4 in l > (sans for !), dans ce cas-là, ça permet de voir si 4 est à l'intérieur de ce groupe-là mais si j'avais mis < 5 in l >, ça aurait été faux. Ça vaut pour les lettres.

word = input("Entre un mot : ")
count = 0

#pas nécessaire : for v in voyelles : 
for elem in word :
    if "a" == elem or "e" == elem or "i" == elem or "o" == elem or "u" == elem or "y" == elem :
        count = count + 1
print(count)

# corrigé, mais vraiment pas optimisé
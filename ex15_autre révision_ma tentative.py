user_number = input("Entre un nombre entre 1 et 100 : ")
user_number = int(user_number)

while user_number < 1 or user_number > 100 :
    user_number = input("Non ! Un nombre entre 1 et 100 : ")
    user_number = int(user_number)

sum = 0

for i in range(0, user_number+1) :
    sum += i
    
print(sum) #pas mettre dans la boucle sinon il affiche chaque étape

#Résultat correct !
    
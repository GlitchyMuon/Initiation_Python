answer = input("Saisissez un nombre : ")
answer = int(answer)
answers = []

if answer > 10:
    print("Ce nombre est plus grand que 10.")
    answer = input("Tapez un nombre : ")
    answers.append(answer)

elif answer <= 10 : 
    print("Le nombre est plus petit ou égal à 10.")
    
    
print(answers)
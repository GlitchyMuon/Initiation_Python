answer = input("Écrivez un nombre entre 1 et 10 : ")
answer = int(answer)

while answer <1 or answer> 10:
    answer = input("Écrivez un nombre entre 1 et 10 : ")
    answer = int(answer) #important de remettre le answer = int(answer)
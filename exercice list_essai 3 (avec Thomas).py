numbers = [87, 13, 64, 57, 29, 73]
answer = int(input("Entre un nombre entre 0 et 5: ")) #à terme : mettre str(len(numbers) -1) au lieu du nombre car la liste peut changer
while answer < 0 or answer > len(numbers) -1 : # 5 était pas incorrect mais à terme on exige >= len(variable_list). > len(variable_list) -1 est ok aussi
    print("Nombre incorrect.")
    answer = int(input("Entre un nombre entre 0 et 5: "))
print(numbers)
print(numbers[0 : answer])
print(numbers[answer : len(numbers)])
numbers_list = []

number = input("Entre des nombres : ")
number = int(number)
numbers_list.append(number)

while len(numbers_list) != 2 :
    number = input("Entre des nombres : ")
    number = int(number)
    numbers_list.append(number)

    while numbers_list[-1] != numbers_list[-2]:

        number = input("Entre des nombres : ")
        number = int(number)
        numbers_list.append(number)

print(str(numbers_list[-1]) + " + " + str(numbers_list[-2]) + " = " + str(numbers_list[0] + numbers_list[1]))


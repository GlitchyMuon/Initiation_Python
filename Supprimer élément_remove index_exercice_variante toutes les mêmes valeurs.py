numbers= [5, 4, 1, 2, 3, 5, 1, 3, 2, 4]
print(numbers)
number = int(input("Entre un nombre : "))
while number > 1 or number < 5 :
    numbers.remove(number)
    print("Incorrect")
    number = int(input("Entre un nombre : "))

print(numbers)

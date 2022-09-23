from random import randint

letters = ["a", "b", "c", "d", "e", "f"]
code = []
len_code = 4

while len(code) < len_code :
    index = randint(0, len(letters) - 1)
    code.append(letters[index])

print(code)

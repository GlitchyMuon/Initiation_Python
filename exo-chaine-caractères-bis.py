data_file = open(r"data/poeme.txt")
data = data_file.readlines()

count = 0
for line in data:
    if line[-1] == "\n":
        line = line[:-1]
    text = line.split(" ")
    target = input("Choisis un mot dans le poème: ")
    target.lower()
    

    for word in text:
        if word == target:
            count += 1
print(count)

data_file.close()
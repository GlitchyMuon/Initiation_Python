# recuperation des données

data_file = open("data/poeme.txt")
data = data_file.read()
data_file.close()

# traitement des données
count = 0
data = data.split("\n")
for line in data:
    line = line.split(" ")
    for word in line:
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace(";", "")

        if word == "Dieu":
            count += 1
             
print(count)
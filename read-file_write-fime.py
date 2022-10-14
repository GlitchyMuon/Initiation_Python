first_name = input("Prénom: ")
last_name = input("Nom: ")
age = input("Age: ")

data_file = open(r"data/data.dat", "w") # on peut ouvrir en append, utilité pour des logs : open(r"data/data.dat", "a")
data_file.write(first_name + "\n")
data_file.write(last_name + "\n")
data_file.write(age + "\n")

data_file.close()
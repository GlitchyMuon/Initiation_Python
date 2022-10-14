first_name = input("Prénom: ")
last_name = input("Nom: ")

data_file = open(r"data/personal.dat", "a")
data_file.write(first_name + "\n")
data_file.write(last_name + "\n")
data_file.close()


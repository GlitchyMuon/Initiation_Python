groceries_file = open(r"data/groceries.txt")

data = groceries_file.readline()

while data != "":
    if data[-1] == "\n":
        data = data[:-1]
    print("- "  + data)
    data = groceries_file.readline()

groceries_file.close()
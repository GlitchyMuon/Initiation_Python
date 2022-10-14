groceries_file = open(r"data/groceries.txt")
data = groceries_file.readlines()

for line in data:
    if line[-1] == "\n":
        line = line[:-1]
    print("- "  + line)


groceries_file.close()
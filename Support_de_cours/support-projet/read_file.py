grocercies_file = open(r"data/groceries.txt")
grocercies_list = grocercies_file.read()
grocercies_file.close()

print(grocercies_list)

line_1 = [1, 2, 3, 4]
line_2 = [5, 6, 7, 8]
line_3 = [9, 10, 11, 12]
# = grid = [[1, 2, 3, 4],
#          [5, 6, 7, 8],
#          [9, 10, 11, 12]]

grid = [line_1, line_2, line_3]

for line in range(3):
    line_txt = "" #il va vider à chaque fois qu'il recommence la boucle
    for column in range(4):
        line_txt = line_txt + str(grid[line][column] /2) + " "
    print(line_txt + "\n")

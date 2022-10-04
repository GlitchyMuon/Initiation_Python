grid = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]]

for line in range(3):
    line_txt = ""
    for column in range(4):
        line_txt = line_txt + str(grid[line][column]//2) + " "

    print(line_txt)
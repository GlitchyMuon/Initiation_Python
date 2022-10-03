line_1 = [1, 2, 3, 4]
line_2 = [5, 6, 7, 8]
line_3 = [9, 10, 11, 12]


grid = [line_1, line_2, line_3]

for line in range(3):
    num = "" 
    for column in range(4):
        num = num + str(grid[line][column])

    print(str(int(num)// 2) + "\n") # pas bon car là je divise la ligne, au lieu de chaque élément du grid

    

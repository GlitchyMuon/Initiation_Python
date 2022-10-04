def gridvalue_add(n):
    for line in range(len(grid)):
        index = line[index]
        sum_line1 = int(line_1[0] + line_1[1] + line_1[2])
        sum_line2 = int(line_2[0] + line_2[1] + line_2[2])
        sum_line3 = int(line_3[0] + line_3[1] + line_3[2])
        n = int(sum_line1 + sum_line2 + sum_line3)
        
    return n

line_1 = [1, 2, 3]
line_2 = [4, 5, 6]
line_3 = [7, 8, 9]

grid = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]

value = gridvalue_add(grid)

print(str(gridvalue_add(grid)))
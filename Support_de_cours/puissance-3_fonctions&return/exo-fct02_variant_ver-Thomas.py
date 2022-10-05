def sum_grid(grid):

    sum_values = 0

    for line in grid:
        for value in line:
            sum_values = sum_values + value

    return sum_values

# -- main --

table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

print(sum_grid(table)) 



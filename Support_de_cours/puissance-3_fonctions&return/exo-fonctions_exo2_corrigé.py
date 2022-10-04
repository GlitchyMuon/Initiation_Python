def sum_grid(grid):
    
    sum_values = 0
    
    for line in range(len(grid)):
        
        for column in range(len(grid[grid])):
            sum_values = sum_values + grid[line][column]
            
    return sum_values

table = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]


def sum_grid(grid):
    
    sum_values = 0
    
    for line in grid :
        
        for value in line :
            sum_values = sum_values + value 
            #à la première itération de la première boucle : value va être 1; sum_values = 1, puis la deuxième itération va être 2, SV =3 la somme sera 3. Ensuite value sera 4 + 3.
            # Addition successive. On boucle sur les valeurs
            
    return sum_values

table = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]
print(sum_grid(table)) 

#  --- functions ---

 #si l'argument reste de couleur terne à la fin, c'est qu'il n'y a pas besoin de l'argument



def display(grid):
    for line in range(len(grid)):
        display_line = str(line) + " "
        
        for column in range(len(grid[line])):
            display_line = display_line + grid[line][column] + " "
        print(display_line)
    print("  0 1 2 3 4") # 2 espaces car chiffre + espace
    # Ou mieux car si changement de len column:
    # end_line = "  "
    # for column in range(len(grid[0])):
    #      end_line = end_line + str(column) + " "
    # print(end_line)

# --- main ---

game = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]]

display(game)


#  --- functions ---

 #si l'argument reste de couleur terne à la fin, c'est qu'il n'y a pas besoin de l'argument
from tracemalloc import get_traced_memory


def display(grid):
    for line in range(len(grid)):
        display_line = ""
        for column in range(len(grid[line])):
            display_line = display_line + grid[line][column] + " "
        print(display_line)


# --- main ---

game = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]]

display(game)


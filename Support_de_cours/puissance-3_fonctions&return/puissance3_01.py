# --- functions ---

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
    [".", ".", ".", "X", "."],
    [".", ".", ".", ".", "."]]

display(game)
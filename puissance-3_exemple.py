for line in range(3):
    txt = ""
    for column in range(3):
        txt = txt + grid[line][column]
    #         " "       
    print(txt + "\n") #passage à la ligne print("a \b") affichera a puis b à la ligne
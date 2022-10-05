
def multiple_table(num):

    for count in range(1, 11):
        
        print(f"{count} x {num} = {count * num}")
        #pas besoin de définir : count = 0          count = count + 1       car la variable après for va parcourir la range(1,11) en commençant par 1 ! ça marche mais doublon et allonge le code pour rien !

    

multiple_table(5)

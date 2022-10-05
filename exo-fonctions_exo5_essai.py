def num_chosen_letter(word, letter):
    count = 0 #important de la mettre en dehors de la boucle for ! Sinon il va m'afficher tout séparément et rajouter un zéro de trop à la fin
    for l in word:
        if l == letter :
            count += 1
            
    return count 

print(num_chosen_letter("aramsamsam", "a"))

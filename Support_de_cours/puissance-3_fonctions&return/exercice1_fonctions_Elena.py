# Créer une fonction qui prend un mot argument et qui renvoie le mot inversé.
# Dans le programme principale, demander à l'utilisateur de saisir un mot au clavier et afficher le mot inverse.

# --- functions ---

def reverse_word(word):
    r_word = ""
    for letter in word:
        r_word = letter + r_word
    return r_word

# --- main ---

word = input("Provide a word: ")
print(reverse_word(word))
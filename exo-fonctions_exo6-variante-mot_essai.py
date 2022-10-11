def without_vowels(word):
    vowels = ["a", "e", "i", "u", "o", "y"]
    consonnants_word = ""
    for v in word:
        if v not in vowels:
            consonnants_word = consonnants_word + v
    return consonnants_word
        
print(without_vowels("anticonstitutionnellement"))

# pour transformer mon mot en liste, il faut faire un casting comme int() ou str() -> list(word)
    
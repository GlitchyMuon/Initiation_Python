def without_vowels(word):
    vowels = ["a", "i", "u", "e", "o", "y"]
    consonnants_list = []
    for v in word:
        if v not in vowels:
            consonnants_list.append(v)
    return consonnants_list
        
print(without_vowels("anticonstitutionnellement"))

# pour transformer mon mot en liste, il faut faire un casting comme int() ou str() -> list(word)
    
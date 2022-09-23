user_word = None
words_list = []

while user_word != "stop":
    user_word = input("mot: ")
    if user_word[0] == "p":
        words_list.insert(0, user_word)

print(words_list)
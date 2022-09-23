user_word = input("mot: ")

words_list = []

while user_word != "stop":
    if user_word[0] == "p":
        words_list.append(user_word)
    user_word = input("mot: ")

print(words_list)
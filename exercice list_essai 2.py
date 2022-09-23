emoji = ["👽", "💩", "🦎", "🌱", "🦠", "🍄"]
from random import randint
index = randint(0, len(emoji)- 1) #Dans ce cas, 5 marche aussi
print(emoji)
print(emoji[index])
print(index)
from random import randint
l = [randint(1, 6), randint(1, 6), randint(1, 6)]


print(l)

while l[0]!= l[1] or l[0] != l[2] :
    l = [randint(1, 6), randint(1, 6), randint(1, 6)]
    print(l)
    

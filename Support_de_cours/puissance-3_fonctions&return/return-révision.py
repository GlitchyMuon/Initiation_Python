from random import randint
def test():
    result = randint(1,6)
    if result < 4:          #si on veut écrire ces3 lignes en une : return result < 4
        return True
    return False
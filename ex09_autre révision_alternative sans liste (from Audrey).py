from random import randint

rdm1 = randint(1,6)
rdm2 = randint(1,6)
rdm3 = randint(1,6)

combinaison = (rdm1, rdm2, rdm3)

while (rdm1 != rdm2) or (rdm1 != rdm3):

    rdm1 = randint(1,6)
    rdm2 = randint(1,6)
    rdm3 = randint(1,6)

    combinaison = (rdm1, rdm2, rdm3)

print(combinaison)
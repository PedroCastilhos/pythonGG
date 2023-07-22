import random

import random

n = random.randint(0,5)

escolhido = 7

chance = 0

while escolhido != n:
    escolhido = int(input('Escolha um número de 1 a 5: '))    
    if escolhido == n: print("Você acertou, o número era {}".format(n))
    else: print("Você errou o número, tente novamente!")
    chance = chance + 1
print('Você utilizou o total de {} chance(s).'.format(chance))
print('Fim')


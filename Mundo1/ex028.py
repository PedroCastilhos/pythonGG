import random

n = random.randint(0,5)

escolhido = int(input("Escolha um número: "))

if escolhido == n: print("Parabéns, você acertou o número")
else: print("Infelizmente você errou!")

print("O número é {}.".format(n))
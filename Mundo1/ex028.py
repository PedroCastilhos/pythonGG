# 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

n = random.randint(0,5)

escolhido = int(input("Escolha um número: "))

if escolhido == n: print("Parabéns, você acertou o número")
else: print("Infelizmente você errou!")

print("O número é {}.".format(n))
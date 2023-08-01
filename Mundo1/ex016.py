# 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

n = float(input("Digite um número com ponto: "))

arr = math.trunc(n)

print("Número escolhido {}".format(n))
print("Número arredondado {}".format(arr))
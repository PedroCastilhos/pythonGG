# 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

if (n1 > n2 and n1 > n3): print('{} É o maior número.'.format(n1))
if (n2 > n1 and n2 > n3): print('{} É o maior número.'.format(n2))
if (n3 > n2 and n3 > n1): print('{} É o maior número.'.format(n3))
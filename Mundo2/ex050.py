# 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

n = 0
soma = 0

for c in range(0,6):
    n = int(input('Escolha um número: ')) 
    if n % 2 == 0: soma = n + soma

print(soma)
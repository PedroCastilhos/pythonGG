# 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input("Número: "))
resultado = n
multiplicador = n


while n != 1:
     n = n - 1
     resultado = resultado * n
     

print("O fatorial de {} é {}".format(multiplicador,resultado))

# 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input("Número: "))
resultado = n
fatorial = 1

for c in range(1,n):      
      resultado = resultado * c


print("O fatorial de {} é {}".format(n,resultado))
# 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso = 0
maior = 0
menor = 1000

for c in range(0,5):
    peso = int(input("PESO: "))    
    if peso < menor: menor = peso
    if peso > maior: maior = peso

print("Menor: {}".format(menor))
print("Maior: {}".format(maior))
# 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

name = input('Frase: ')

print(name.count('a'))

print(name.find('a')+1) 
print(name.rfind('a')+1) 

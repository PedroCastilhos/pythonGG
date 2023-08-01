# 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

ano = 0
maior = 0

for c in range(0,4):
  ano = int(input("Ano de nascimento: "))
  if ano > 2005: maior = maior + 1

print("{} pessoas são maiores de idade.".format(maior))
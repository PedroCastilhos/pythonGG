#54

ano = 0
maior = 0

for c in range(0,4):
  ano = int(input("Ano de nascimento: "))
  if ano > 2005: maior = maior + 1

print("{} pessoas são maiores de idade.".format(maior))
# 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dis = int(input("A distancia de uma viagem: "))

valor = 0

if dis < 200: valor = dis*0.50
else: valor = dis * 0.45

print(valor)
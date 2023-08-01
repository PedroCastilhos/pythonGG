# 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input("Velocidade: "))

if vel > 80: print('Você foi multado, e deverá pagar {} reais de multa'.format((vel - 80)*7))
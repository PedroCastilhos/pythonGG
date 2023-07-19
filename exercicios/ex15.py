#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input("Quantos dias alugado? "))
km = int(input("Quantos Km rodados? "))

Rkm = km * 0.15
Rdias = dias * 60

print('O preço a pagar no total é de:', Rkm + Rdias)

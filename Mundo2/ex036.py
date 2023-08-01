# 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = int(input("Valor da casa: "))

salario = float(input("Salário: "))

anos = int(input("Quantos anos de empréstimo: "))

meses = anos * 12

prestacao = casa / meses

resposta = salario * 0.3 / 100


# 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

n = int(input('Preco do produto: '))

desconto = (n * 5) / 100

print('O valor do produto do produto com 5% de descnonto é de', n - desconto )
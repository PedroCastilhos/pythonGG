# 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

n1 = int(input('Altura da parede: '))
n2 = int(input('Largura da parede: '))

area = n1 * n2

print('Para pintar toda a parede será necessário', area / 2 ,'Litros de tinta.')
# 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

cat1 = int(input("Informe o valor do primeiro cateto: "))
cat2 = int(input("Informe o valor do segundo cateto: "))

cat11 = math.pow(cat1,2)
cat22 = math.pow(cat2,2)

hip = cat11 + cat22
resposta = math.sqrt(hip)
print(resposta)
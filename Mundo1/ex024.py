# 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

city = input("Nome da cidade: ")

lista = city.split()

print(lista[0].find('Santo'))
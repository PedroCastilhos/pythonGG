# 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

name = input("Nome: ")

print(name)

lista = name.split()

print(lista[0])

print(lista[len(lista)-1])
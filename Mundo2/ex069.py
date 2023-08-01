# 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

idade = 0
sexo = 'f'
maiores = 0
man = 0
woman = 0

while True:
    sexo = input("Sexo [F/M]: ")
    idade = int(input('Idade: '))
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        man += 1
    if idade < 20 and sexo == "F":
        woman += 1
    seguir = input("Seguir? [S/N]")
    if seguir == "N":
        break
    
print("===========")
print(f'{maiores} maior de 18 anos')
print(f'{man} homens')
print(f'{woman} mulheres com menos de 20 anos')
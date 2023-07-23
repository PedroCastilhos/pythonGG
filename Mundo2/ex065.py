#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = 0
total = 0
contagem = 0
maior = 0
menor = 99999999999999999999999999999999999999
media = 0
sair = ''

while sair != 'sair':
    n = int(input("Número: "))
    total = total + n
    contagem = contagem + 1
    if n < menor: menor = n
    if n > maior: maior = n
    media = total / contagem
    print('O maior número digitado é {}'.format(maior))
    print('O menor número digitado é {}'.format(menor))
    print('A média dos números digitados é {}'.format(media))
    sair = input('Digite ''sair'' para encerrar ou "continuar" para seguir o programa!')

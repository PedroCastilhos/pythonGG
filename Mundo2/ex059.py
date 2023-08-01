# 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
# sair = 0

while sair != 5:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))  
    print("Escolha uma das operações para realiza-la:")
    sair = int(input('[1] para SOMAR \n[2] para MULTIPLICAR\n[3] ver o MAIOR entre eles\n[4] TROCAR os números\n[5] SAIR do programa\n '))
    if sair == 1: print('A soma de {} e {} é {}.'.format(n1,n2,n1+n2))
    if sair == 2: print('A multiplicação de {} e {} é {}.'.format(n1,n2,n1*n2))
    if sair == 3: 
        if n1 > n2: print('O número {} é maior que o {}'.format(n1,n2))
        if n2 > n1: print('O número {} é maior que o {}'.format(n2,n1))
    if sair == 5: sair = 5           
print('Fim')

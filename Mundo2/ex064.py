#64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 0
contagem = 1
soma = 0

while n != 999:
    n = int(input("Número: "))
    if n != 999: 
      soma = soma + n
      contagem = contagem + 1

print('Foram digitado(s) {} número(s)'.format(contagem - 1))
print('A soma de todos os números é {}'.format(soma))
      
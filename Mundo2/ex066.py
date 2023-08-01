# 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n = 0
contagem = 0
soma = 0

while n != 999:
    n = int(input("Número: "))
    contagem += 1
    soma += n

print(f'A soma dos números digitados foi de {soma - 999}')
print(f'A contagem dos números digitados foi de {contagem -1 }')
#66

n = 0
contagem = 0
soma = 0

while n != 999:
    n = int(input("Número: "))
    contagem += 1
    soma += n

print(f'A soma dos números digitados foi de {soma - 999}')
print(f'A contagem dos números digitados foi de {contagem -1 }')
#
total = 0
caro = 0
preco = 0
nome = ''
maisCaro = ''
valorCaro = 0

while True:
    nome = input("Nome do produto: [FIM para sair] ")
    preco = int(input("Valor do produto: "))
    total += preco    
    if preco > 1000:
        caro += 1
    if preco > valorCaro:
        valorCaro = preco
        maisCaro = nome
    if nome == "FIM":
        break

print("===============")
print(f"O total gasto foi de {total}")
print(f"O número de produtos que custam mais de R$1000,00: {caro}")
print(f"O produto mais caro é o {maisCaro} e custa {valorCaro}")

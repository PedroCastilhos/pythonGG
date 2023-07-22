dis = int(input("A distancia de uma viagem: "))

valor = 0

if dis < 200: valor = dis*0.50
else: valor = dis * 0.45

print(valor)
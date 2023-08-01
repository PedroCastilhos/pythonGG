# 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
valor = int(input("Valor para ser sacado: "))
nota50 = 0
nota20 = 0
nota10 = 0
sobra = 0

while True:
    if valor < 10:
        break
    if valor % 50 == 0:
        print(f"O seu saque terá {valor/50} notas de R$50")
    elif valor % 20 == 0:
        print(f"O seu saque terá {valor/20} notas de R$20")
    elif valor % 10 == 0:
        print(f"O seu saque terá {valor/10} notas de R$10")
    else:
      if valor % 50 != 0:
          nota50 = valor /50
          sobra = valor % 50
          nota20 = sobra / 20
          sobra += valor % 20
          nota10 = sobra /10
          if valor % 10 != 0:
              print(f"{valor % 10 != 0} do valor não poderá ser sacado")
    break



print("========== FIM ==========")
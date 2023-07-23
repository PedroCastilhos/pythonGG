#68
import random
derrota = 0
pc = 0
vitoria = 0
valor = 0
contagem = 0

while derrota == 0:
    pc = random.randint(1,2)
    print(pc)
    valor = int(input("Digite um valor: "))
    cond = input("Par ou Ímpar? [P/I]: ")
    resultado = valor + pc
    print(f'Você jogou {valor} e o computador {pc}. Total de {valor + pc}')
    if  cond == 'P' and resultado % 2 == 0: 
        contagem += 1       
        vitoria += 1
        print("Você venceu!")
    elif cond == 'I' and resultado % 2 == 1:
        print("Você venceu!")
        vitoria += 1
        contagem += 1
    elif cond == 'P' and resultado % 2 == 1:
      print('Derrota')
      print(f"Voce venceu {contagem}x")
      break
    else: 
       print('Derrota')
       print(f"Voce venceu {contagem}x")
       break

    
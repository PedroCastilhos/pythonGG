# 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")

nR = random.randint(1,4)

if nR == 1: print("Aluno {} deverá apagar o quadro".format(n1))
if nR == 2: print("Aluno {} deverá apagar o quadro".format(n2))
if nR == 3: print("Aluno {} deverá apagar o quadro".format(n3))
if nR == 4: print("Aluno {} deverá apagar o quadro".format(n4))


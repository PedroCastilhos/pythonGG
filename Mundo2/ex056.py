n1 = input('Nome 1: ')
n2 = input('Nome 2: ')
n3 = input('Nome 3: ')
n4 = input('Nome 4: ')

listaNome = [n1,n2,n3,n4]

i1 = int(input('idade1: '))
i2 = int(input('idade2: '))
i3 = int(input('idade3: '))
i4 = int(input('idade4: '))

listaIdade = [i1,i2,i3,i4]
print('A Idade média é: ', (i1 + i2 + i3 + i4) /4)

s1 = input('Sexo1: ')
s2 = input('Sexo2: ')
s3 = input('Sexo3: ')
s4 = input('Sexo4: ')

listaSexo = [s1,s2,s3,s4]

velho = 0
nomeVelho = 'teste'

for c in range(0,4):
    if listaSexo[c] == 'm':
      if listaIdade[c] > velho: 
        velho = listaIdade[c]
      nomeVelho = listaNome[c]


novas = 0
for c in range(0,4):
   if listaSexo[c] == 'f':
      if listaIdade[c] < 20:
         novas = novas + 1


print('O homem mais velho é o {} com {} anos'.format(nomeVelho,velho))
print('{} Mulheres tem menos que 20 anos'.format(novas))
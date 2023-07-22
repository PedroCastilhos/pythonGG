#56

while sexo == 'M' or 'F' or 'm' or 'f':
    pergunta = input('Digite um sexo [M/F]: ')
    sair = input("Digite FIM para sair: ")
    if sair == 'fim': sexo = 'break'
    if pergunta != 'M' or 'F' or 'm' or 'f': print('Digire M ou F corretamente! ')
print('Fim do programa:')



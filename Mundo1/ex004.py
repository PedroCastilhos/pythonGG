n = input('Digite algo: ')

#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

#Saber o tipo primitivo do elemento
print(type(n))

#Número
print('Número? ', n.isnumeric())

#Alfabeto
print('Letra? ', n.isalpha()) 

#Número ou letra
print('Letra ou número? ' ,n.isalnum)

#Letra maiuscula
print('Letra maíuscula? ', n.isupper())

#Letra minuscula
print('Letra minuscula? ', n.islower)

#Contem espaço
print('Contém espaço(s) ', n.isspace)
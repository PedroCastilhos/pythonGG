n = input('Digite algo: ')

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
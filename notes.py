#Strings

frase = 'Curso em vídeo Python' #20 caracteres

print(frase[9]) #Pegaria só o 9 elemento

print(frase[9:13]) #Pegaria só do 9 ao 12 elementos, começo é certo, mas no final ele faz um a menos

print(frase[9:21]) #Pegaria do 9 elemento até o fim

print(frase[9:21:2]) #Mesma coisa do de cima, só que "pulando" de 2 caracteres

print(frase[:5]) #Pega do começo até o 5, é a mesma coisa que 0:5

print(frase[15:]) #Pega do 15 até o final

print(frase[9::3]) #9: = vai até o final | :3 vai pulando de três em três

print(len(frase)) #Número de caracteres que possui a string

print(frase.count('o')) #Conta quantas vezes aparece o caractere 'o'
print(frase.count('o',0,13)) #Conta quantas vezes aparece o caractere 'o' do caractere 0 ao 12
print(frase.find('deo')) #11

print(frase.find('Android')) #Vai retornar -1

print('Curso' in frase) #Vai retornar true

print(frase.replace('Python','Android')) #Substitui o Python por Android

print(frase.upper()) #Vai deixar a frase toda em maíusculo

print(frase.lower()) #Deixa tudo minusculo

print(frase.capitalize()) #Deixa todo os caracteres em minusculos com exceção do primeiro

print(frase.title()) #A cada palavra(depois de um espaço) ele vai deixar a primeira letra em maíusculo

print(frase.strip()) #Remove todos os espaços inuteis 

print(frase.rstrip()) #Remove somente os espaços da direita

print(frase.lstrip()) #Remove somente os espaços da esquerda

print(frase.split()) #Vai criar uma lista com cada palavras dos caracteres ['curso','em','video','python']

print('-'.join(frase)) #Curso-em-video-python


print("""xxxx
      xxxx
      xxxx""") #Mesmo quebrando a linha, tudo vai pro print



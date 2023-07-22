#47

n = int(input("Escolha uma tabuada: "))

for c in range(1,11):
    print('{} X {} = {}'.format(n,c,c*n))
print('Fim')
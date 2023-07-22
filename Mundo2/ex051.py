#Progressão aritmética

n = int(input("Número: "))

primo = 0

for c in range(1,n):
    if n % c == 0: primo = primo + c


if primo > 2: print("{} não é um número primo.".format(n))
else: print("{} É um número primo".format(n))
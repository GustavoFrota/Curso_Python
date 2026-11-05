n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2

#print(f'O resultado da soma é {s}')

print('O resultado da soma é {}'.format(s))
print(type(s)) #Inteiro

print('A soma entre {} e {} vale {}'.format(n1, n2, s))
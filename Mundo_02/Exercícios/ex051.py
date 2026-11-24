numero = int(input('Digite um número: '))
count = 0

for n in range(1, numero+1):
    print(n, end=' ')
    if numero % n == 0:
        count += 1

print()

if count == 2:
    print(f'O número {numero} foi divisível 2 vezes')
    print('Por isso, ele é PRIMO')
else:
    print(f'O número {numero} foi divisível {count} vezes.')
    print('Por isso, ele NÃO É PRIMO')
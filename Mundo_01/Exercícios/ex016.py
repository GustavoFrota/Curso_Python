from math import floor

numero = float(input('Digite um número real: '))
n1 = floor(numero)

print(f'O valor digitado foi {numero} e a sua porção inteira é {n1}')

outro = float(input('Digite outro número real: ')) # Sem o módulo math
print(f'O valor digitado foi {outro} e a sua porção inteira é {int(outro)}')
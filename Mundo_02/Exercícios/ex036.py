numero = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] coverter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input('Sua opção: '))

if escolha == 1:
    binario = bin(numero)[2:]
    print(f'{numero} convertido para BINÁRIO é igual a {binario}')
elif escolha == 2:
    octal = oct(numero)[2:]
    print(f'{numero} convertido para OCTAL é igual a {octal}')
elif escolha == 3:
    hexadecimal = hex(numero)[2:]
    print(f'{numero} convertido para HEXADECIMAL é igual a {hexadecimal}')
else:
    print('Escolha apenas uma das opções acima!')
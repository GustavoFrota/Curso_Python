''' nome = str(input('Digite o seu nome: ')).title().strip()

if nome == 'Gustavo':
    print('Que nome legal!')
else:
    print('Seu nome é tão normal!')

print(f'Seja bem-vindo {nome}.')
print('---Fim do programa---')  '''

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print(f'A média foi {media}')

if media >= 7:
    print('Aprovado!')
    print('Parabéns!')
else:
    print('Reprovado!')
    print('EStude mais!')
print('---FIM---')
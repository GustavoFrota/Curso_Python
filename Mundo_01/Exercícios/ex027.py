from random import randint
from time import sleep
computador = randint(0, 5)

print('Computador: Tente adivinhar o número que estou pensando de 0 a 5')
numero = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(3)
print(f'Computador: Eu pensei no número {computador}')

if numero == computador: 
    print('Computador: Você acertou!')
else:
    print('Computador: Você errou!')
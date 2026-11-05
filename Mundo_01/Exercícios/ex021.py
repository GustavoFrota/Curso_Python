frase = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome...')

print(f'O seu nome em maiúsculas é {frase.upper()}')
print(f'O seu nome em minúsculas é {frase.lower()}')
print(f'O seu nome tem ao todo {len(frase) - frase.count(' ')} letras')
print(f'O seu primeiro nome tem {frase.find(' ')} letras')
peso = float(input('Digite o seu peso: (KG)'))
altura = float(input('Digite a sua altura: (M)'))
imc = peso / (altura ** 2)
print(f'O IMC da pessoa é {imc:.1f}')

if imc < 18.5:
    print('Você está em ABAIXO DO PESO')
elif imc <= 25:
    print('Você está em PESO IDEAL')
elif imc <= 30:
    print('Você está em SOBREPESO')
elif imc <= 40:
    print('Você está em OBESIDADE')
else:
    print('Você está em OBESIDADE MÓRBIDA')
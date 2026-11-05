local = float(input('Qual a distância de sua viagem? '))
print(f'Você está prestes a fazer uma viagem de {local}km')

if local <= 200:
    perto = local * 0.5
    print(f'E o preço de sua passagem será de R${perto:.2f}')
else:
    longe = local * 0.45
    print(f'E o preço de sua passagem será de R${longe:.2f}')
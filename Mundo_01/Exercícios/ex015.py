dias = int(input('Quantos dias alugados? '))
aluguel = dias * 60
km = int(input('Quantos Km rodados? '))
rodados = km * 0.15

print(f'O total a pagar é de R${aluguel + rodados:.2f}')

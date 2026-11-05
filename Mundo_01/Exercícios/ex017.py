cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

co = cateto_oposto ** 2
ca = cateto_adjacente ** 2

hipotenuza = (ca + co) ** 0.5

print(f'A hipotenuza vai medir {hipotenuza:.2f}')
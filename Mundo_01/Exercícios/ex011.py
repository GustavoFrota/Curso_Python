la = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = la * alt
tinta = area / 2

print(f'Sua parede tem uma dimensão de {la}X{alt} e sua área é de {area}m²')
print(f'Para pintar essa parede você vai precisar de {tinta}L de tinta')
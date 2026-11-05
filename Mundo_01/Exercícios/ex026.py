nome = str(input('Digite seu nome completo: ')).strip().title()
partes = nome.split()
primeiro_nome = partes[0]
ultimo_nome = partes[-1]

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu último nome é {ultimo_nome}')

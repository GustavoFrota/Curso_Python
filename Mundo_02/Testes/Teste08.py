nome = str(input('Digite o seu nome: ')).title().strip()
if nome == 'Gustavo':
  print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
  print('Seu nome é bastante popular no Brasil!')
else:
  print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}!')
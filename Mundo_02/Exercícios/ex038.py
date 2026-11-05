from datetime import date

ano = int(input('Ano de nascimento: '))
hoje = date.today().year
idade = hoje - ano

print(f'Quem nasceu em {ano} tem {idade} anos em {hoje}')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para se alistar')
elif idade > 18:
    saldo = idade - 18
    print(f'Você deveria ter se alistado há {saldo} anos')

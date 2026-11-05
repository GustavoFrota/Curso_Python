salario = float(input('Digite o salário do funcionário: R$'))

if salario > 1250:
    aumento = (salario * 10) / 100
    novo_salario = salario + aumento
    print(f'Seu salário que antes era R${salario:.2F} agora é R${novo_salario:.2F}')
else:
    aumento = (salario * 15) / 100
    novo_salario = salario + aumento
    print(f'Seu salário que antes era R${salario:.2F} agora é R${novo_salario:.2F}')
valor = float(input('Valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
ano = int(input('Quantos anos de financiamneto? '))

prestacao = valor / (ano * 12)
limite = salario * 0.30

print(f'Prestação mensal: R${prestacao:.2f}')
print(f'Limite de 30% do salário: R${limite:.2f}')

if prestacao <= limite:
    print('Empréstimo aprovado')
else:
    print('Empréstimo reprovado')
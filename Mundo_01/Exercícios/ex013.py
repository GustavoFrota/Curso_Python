salario = float(input('Digite o salário do funcionário: R$'))
aumento = (salario * 15) / 100

print(f'Um funcionário que ganhava R${salario}, com desconto de 15%, passa a receber R${salario + aumento:.2f}')
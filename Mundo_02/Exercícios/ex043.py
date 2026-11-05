print('====== LOjas Freitas ======')
preco = float(input('Preço das compras: R$'))

print("""FORMAS DE PAGAMENTO
( 1 ) à vista dinheiro/cheque
( 2 ) à vista cartão
( 3 ) 2x no cartão
( 4 ) 3x ou mais no cartão""")
forma = int(input('Qual a opção? '))

if forma == 1:
    valor = (preco * 10) / 100
    print(f'Sua compra de R${preco:.2f} vai custar R${preco - valor:.2f} no final')
elif forma == 2:
    valor = (preco * 5) / 100
    print(f'sua compra de R${preco:.2f} vai custar R${preco - valor:.2f} no final')
elif forma == 3:
    valor = preco / 2
    print(f'Sua compra será parcelada em 2x de R${valor:.2f}')
elif forma == 4:
    parcela = int(input('Quantas parcelas? '))
    valor = preco / parcela
    juros = (preco * 20) / 100
    print(f'Sua compra será parcelada em {parcela}x de R${valor:.2f}')
    print(f'Com juros sua compra de R${preco:.2f} vai custar R${preco + juros:.2f} no final')
else:
    print('Forma de pagamento inválido! Tente novamente')
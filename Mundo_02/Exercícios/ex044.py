from random import choice

print("""Suas opções
( 0 ) PEDRA
( 1 ) PAPEL
( 2 ) TESOURA""")
escolha = int(input('Qual é a sua jogada? '))

opções = [ 0, 1, 2]
computador = choice(opções)

if escolha == 0:
    print('O jogador escolheu PEDRA')
    if computador == 0:
        print('O computador escolheu PEDRA! EMPATE')
    elif computador == 1:
        print('O computador escolheu PAPEL!')
        print('O computador Venceu!')
    else:
        print('O computador escolheu TESOURA!')
        print('O jogador vence!')
elif escolha == 1:
    print('O jogador escolheu PAPEL')
    if computador == 0:
        print('O computador escolheu PEDRA!')
        print('O jogaador vence')
    elif computador == 1:
        print('O computador escolheu PAPEL! EMPATE')
    else:
        print('O computador escolheu TESOURA!')
        print('O computador venceu!')
elif escolha == 2:
    print('O jogador escolheu TESOURA!')
    if computador == 0:
        print('O computador escolheu PEDRA!')
        print('O computador venceu!')
    elif computador == 1:
        print('O computador escolheu PAPEL!')
        print('O jogador vence!')
    else:
        print('O computador escolheu TESOURA! EMPATE')
else:
    print('Opção inválida! Tente novamente')
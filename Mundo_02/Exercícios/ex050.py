print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)

ter1 = int(input('Digite o primeiro termo: ')) #Termo 1
raz = int(input('Digite a razão: ')) #Razão

for n in range(1, 11):
    print(ter1, end=' -> ')
    ter1 += raz
print('Acabou')
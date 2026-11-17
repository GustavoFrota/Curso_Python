print('='*30)
print('10 TERMOS DE UMA PA')
print('='*30)

ter1 = int(input('Digite o primeiro termo: ')) #Termo 1
raz = int(input('Digite a razão: ')) #Razão

for n in range(ter1, 20, raz):
    ter1 += ter1 + raz
    print(n, end=' -> ')
print('Acabou')
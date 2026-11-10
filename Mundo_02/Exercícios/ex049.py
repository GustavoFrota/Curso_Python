soma = 0
count = 0

for c in range(1, 7):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        soma += numero
        count += 1

print(f'Você informou {count} números PARES e a soma foi {soma}')
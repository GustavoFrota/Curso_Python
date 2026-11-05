print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('Os segmentos acima podem formar um triângulo!')
    if s1 == s2 == s3:
      print('Triângulo Equilátero')
    elif s1 != s2 != s3 != s1:
       print('Triângulo Escaleno')
    else:
       print('Triângulo Isósceles')
    
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')

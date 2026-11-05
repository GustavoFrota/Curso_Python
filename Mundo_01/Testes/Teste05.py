frase = 'Curso em Vídeo Python'

print(frase[9:15])

print(len(frase))

print(frase.count('o'))

print(frase.find('deo'))
#print(frase.find('Android'))

print(frase.replace('Python', 'Android'))

print(frase.upper())

print(frase.lower())

print(frase.capitalize())

print(frase.title())

frase2 = '  Aprenda Python  '
print(frase2)
print(frase2.rstrip())
print(frase2.lstrip())
print(frase2.strip())


frase3 = frase.split()
print(frase3)

print('-'.join(frase3))
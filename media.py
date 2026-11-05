import pandas as pd

dados = {
    'Nome' : ['Ana', 'João', 'Maria'],
    'Nota1' : [8, 7, 9],
    'Nota2' : [9, 6, 10]
}

df = pd.DataFrame(dados)

#Criando uma tabela chamada Média com base nas tabelas Nota1 mais Nota2 dividido por 2
df['Média'] = (df['Nota1'] + df['Nota2']) / 2


df['Situação'] = df['Média'].apply(
    lambda nota: 'Aprovado' if nota >= 7 else 'Reprovado'
)
print(df)
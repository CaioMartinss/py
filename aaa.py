import pandas as pd

# Passo 1: Ler o arquivo CSV
arquivo_csv = 'transacoes_pix.csv'
df = pd.read_csv(arquivo_csv)

# Passo 2: Converter a coluna 'data' para datetime
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')

# Passo 3: Criar uma tabela pivot com as transações agrupadas por dia e tipo_transacao
pivot_table = df.pivot_table(values='valor', index='data', columns='tipo_transacao', aggfunc='sum', fill_value=0)

# Passo 4: Adicionar coluna com a quantidade de transações por dia
pivot_table['quantidade_transacoes_por_dia'] = df.groupby(['data', 'tipo_transacao']).size().unstack().sum(axis=1)

# Passo 5: Agrupar por mês e somar os valores e a quantidade de transações
pivot_table_por_mes = pivot_table.resample('M').sum()
pivot_table_por_mes['quantidade_transacoes_por_mes'] = df.resample('M', on='data')['tipo_transacao'].count()

# Passo 6: Resetar o índice se desejar ter a coluna 'data'
pivot_table_por_mes = pivot_table_por_mes.reset_index()

# Passo 7: Formatar os valores para o estilo brasileiro (comma separated)
for tipo_transacao in df['tipo_transacao'].unique():
    pivot_table_por_mes[tipo_transacao] = pivot_table_por_mes[tipo_transacao].apply(lambda x: f'{x:.2f}'.replace('.', ','))

# Exibir ou salvar o resultado
print(pivot_table_por_mes)

# Salvar em um novo arquivo CSV com o estilo brasileiro
arquivo_csv_formatado = 'transacoes_agrupadas_4.csv'
pivot_table_por_mes.to_csv(arquivo_csv_formatado, index=False, sep=';', decimal=',')

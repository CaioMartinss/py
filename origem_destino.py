import pandas as pd

# Carregar o arquivo CSV fornecido pelo usuário
df = pd.read_csv('transacoes_pix.csv')

# Visualizar as primeiras linhas para entender a estrutura dos dados
print("Primeiras linhas do DataFrame:")
print(df.head())
print()

# Limpeza e Preparação dos Dados
df['data'] = pd.to_datetime(df['data'], errors='coerce')

# Remover espaços em branco desnecessários nas colunas de origem e destino (se houver)
df['origem'] = df['origem'].str.strip()
df['destino'] = df['destino'].str.strip()

# Contar o número de transações por combinação de origem e destino
transacoes_por_origem_destino = df.groupby(['origem', 'destino']).size().reset_index(name='vezes_que_repetiu')

# Filtrar transações que se repetem mais de 2 vezes
transacoes_por_origem_destino = transacoes_por_origem_destino[transacoes_por_origem_destino['vezes_que_repetiu'] > 2]

# Adicionar coluna de ano
transacoes_por_origem_destino['ano'] = pd.to_datetime(df['data']).dt.year

# Ordenar as combinações pela contagem de transações em ordem decrescente
transacoes_por_origem_destino = transacoes_por_origem_destino.sort_values(by='vezes_que_repetiu', ascending=False)

# Exibir as 10 combinações mais frequentes
print("Top 10 Combinações de Origem e Destino mais Frequentes (repetidas mais de 2 vezes):")
print(transacoes_por_origem_destino.head(10))
print()

# Salvar o DataFrame das combinações em um novo arquivo CSV
transacoes_por_origem_destino.to_csv('transacoes_origem_destino_repetidas.csv', index=False)

# Exibir mensagem de conclusão
print("Análise concluída. Resultados salvos no arquivo transacoes_origem_destino_repetidas.csv.")

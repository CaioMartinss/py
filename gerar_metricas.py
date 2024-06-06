import pandas as pd

# Carregar os dados
df = pd.read_csv('dados.csv')  # Substitua 'seu_arquivo.csv' pelo nome do seu arquivo CSV

# Remover caracteres não numéricos e converter para formato numérico
df['valor_transacao'] = df['valor_transacao'].replace({'R\$ ': '', ',': ''}, regex=True).astype(float)

# Calcular métricas
media = df['valor_transacao'].mean()
mediana = df['valor_transacao'].median()
desvio_padrao = df['valor_transacao'].std()
total_transacoes = df['valor_transacao'].count()
volume_total_transacionado = df['valor_transacao'].sum()

# Criar novo DataFrame com as métricas
metricas_df = pd.DataFrame({
    'Métrica': ['Média', 'Mediana', 'Desvio Padrão', 'Total de Transações', 'Volume Total Transacionado'],
    'Valor': [media, mediana, desvio_padrao, total_transacoes, volume_total_transacionado]
})

# Salvar o novo DataFrame em um novo arquivo CSV
metricas_df.to_csv('metricas.csv', index=False)

print("Novo arquivo 'metricas.csv' criado com sucesso!")

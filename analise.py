import pandas as pd

# Carregar o arquivo CSV fornecido pelo usuário
df = pd.read_csv('transacoes_pix_ordenado.csv')

# Converter a coluna 'data' para datetime
df['data'] = pd.to_datetime(df['data'], errors='coerce')

# Remover o símbolo de moeda e converter 'valor' para float, usando ponto como separador decimal
df['valor'] = df['valor'].replace({'R\$': '', ',': '.'}, regex=True).astype(float)

# Calcular métricas diárias
df['dia'] = df['data'].dt.date
df_daily = df.groupby('dia').agg(
    valor_total_dia=('valor', 'sum'),
    media_valor_dia=('valor', 'mean'),
    mediana_valor_dia=('valor', 'median'),
    desvio_padrao=('valor', 'std'),
    total_transacoes=('valor', 'count'),
    volume_total_transicionado=('valor', 'sum')
).reset_index()

# Calcular métricas semanais
df_daily['semana'] = pd.to_datetime(df_daily['dia']).dt.isocalendar().week
df_weekly = df_daily.groupby('semana').agg(
    valor_total_semana=('valor_total_dia', 'sum'),
    media_valor_semana=('valor_total_dia', 'mean'),
    mediana_valor_semana=('valor_total_dia', 'median')
).reset_index()

# Calcular métricas mensais
df_daily['mes'] = pd.to_datetime(df_daily['dia']).dt.month
df_monthly = df_daily.groupby('mes').agg(
    valor_total_mes=('valor_total_dia', 'sum'),
    media_valor_mes=('valor_total_dia', 'mean'),
    mediana_valor_mes=('valor_total_dia', 'median')
).reset_index()

# Merge das informações semanais e mensais
df_daily = pd.merge(df_daily, df_weekly, on='semana', how='left')
df_daily = pd.merge(df_daily, df_monthly, on='mes', how='left')

# Selecionar e renomear as colunas finais
df_final = df_daily[['dia', 'valor_total_dia', 'valor_total_semana', 'valor_total_mes',
                     'media_valor_dia', 'media_valor_semana', 'media_valor_mes',
                     'mediana_valor_dia', 'mediana_valor_semana', 'mediana_valor_mes',
                     'desvio_padrao', 'total_transacoes', 'volume_total_transicionado']]

# Formatar valores para o formato brasileiro
for col in ['valor_total_dia', 'valor_total_semana', 'valor_total_mes',
            'media_valor_dia', 'media_valor_semana', 'media_valor_mes',
            'mediana_valor_dia', 'mediana_valor_semana', 'mediana_valor_mes',
            'desvio_padrao', 'volume_total_transicionado']:
    df_final[col] = df_final[col].apply(lambda x: f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Salvar o DataFrame resultante em um novo arquivo CSV
df_final.to_csv('transacoes_pix_analise.csv', index=False)

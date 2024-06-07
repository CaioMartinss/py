import pandas as pd

# Carregar o arquivo CSV gerado anteriormente
df = pd.read_csv('transacoes_pix.csv')

# Converter a coluna 'data' para datetime
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')

# Adicionar coluna de tipo de transação
df['tipo_transacao'] = df['tipo_transacao'].astype('category')

# Filtrar transações empresariais e pessoais
df_empresarial = df[df['tipo_transacao'] == 'empresarial']
df_pessoal = df[df['tipo_transacao'] == 'pessoal']

# Função para calcular métricas por dia, semana e mês
def calcular_metricas(df):
    # Métricas por dia
    metricas_dia = df.groupby(df['data'].dt.date).agg({
        'valor': ['sum', 'mean', 'median', 'std', 'count']
    }).reset_index()
    metricas_dia.columns = ['dia', 'valor_total_dia', 'media_valor_dia', 
                            'mediana_valor_dia', 'desvio_padrao_dia', 'total_transacoes_dia']

    # Converter 'dia' para datetime
    metricas_dia['dia'] = pd.to_datetime(metricas_dia['dia'])

    # Criar coluna semana
    metricas_dia['semana'] = metricas_dia['dia'].dt.to_period('W').apply(lambda r: r.start_time)

    # Métricas por semana
    metricas_semana = metricas_dia.groupby('semana').agg({
        'valor_total_dia': 'sum',
        'media_valor_dia': 'mean',
        'mediana_valor_dia': 'median',
        'desvio_padrao_dia': 'std',
        'total_transacoes_dia': 'sum'
    }).reset_index()
    metricas_semana.columns = ['semana', 'valor_total_semana', 'media_valor_semana', 
                               'mediana_valor_semana', 'desvio_padrao_semana', 'total_transacoes_semana']

    # Criar coluna mês
    metricas_semana['mes'] = metricas_semana['semana'].dt.to_period('M').apply(lambda r: r.start_time)

    # Métricas por mês
    metricas_mes = metricas_semana.groupby('mes').agg({
        'valor_total_semana': 'sum',
        'media_valor_semana': 'mean',
        'mediana_valor_semana': 'median',
        'desvio_padrao_semana': 'std',
        'total_transacoes_semana': 'sum'
    }).reset_index()
    metricas_mes.columns = ['mes', 'valor_total_mes', 'media_valor_mes', 
                            'mediana_valor_mes', 'desvio_padrao_mes', 'total_transacoes_mes']

    return metricas_dia, metricas_semana, metricas_mes

# Calcular métricas para transações empresariais e pessoais
metricas_empresarial_dia, metricas_empresarial_semana, metricas_empresarial_mes = calcular_metricas(df_empresarial)
metricas_pessoal_dia, metricas_pessoal_semana, metricas_pessoal_mes = calcular_metricas(df_pessoal)

# Fundir as métricas diárias, semanais e mensais
df_empresarial_final = pd.merge(metricas_empresarial_dia, metricas_empresarial_semana, on='semana', how='outer')
df_empresarial_final = pd.merge(df_empresarial_final, metricas_empresarial_mes, on='mes', how='outer')

df_pessoal_final = pd.merge(metricas_pessoal_dia, metricas_pessoal_semana, on='semana', how='outer')
df_pessoal_final = pd.merge(df_pessoal_final, metricas_pessoal_mes, on='mes', how='outer')

# Selecionar apenas as colunas necessárias
cols_to_keep = ['dia', 'valor_total_dia', 'valor_total_semana', 'valor_total_mes',
                'media_valor_dia', 'media_valor_semana', 'media_valor_mes',
                'mediana_valor_dia', 'mediana_valor_semana', 'mediana_valor_mes',
                'desvio_padrao_dia', 'desvio_padrao_semana', 'desvio_padrao_mes',
                'total_transacoes_dia', 'total_transacoes_semana', 'total_transacoes_mes']

df_empresarial_final = df_empresarial_final[cols_to_keep]
df_pessoal_final = df_pessoal_final[cols_to_keep]

# Salvar em CSV
output_path_empresarial = 'metricas_transacoes_empresariais.csv'
df_empresarial_final.to_csv(output_path_empresarial, index=False)
print(f"Arquivo CSV para transações empresariais salvo em: {output_path_empresarial}")

output_path_pessoal = 'metricas_transacoes_pessoais.csv'
df_pessoal_final.to_csv(output_path_pessoal, index=False)
print(f"Arquivo CSV para transações pessoais salvo em: {output_path_pessoal}")

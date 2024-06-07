import pandas as pd

# Nome do arquivo CSV de entrada e saída
arquivo_entrada = 'transacoes_pix.csv'
arquivo_saida = 'transacoes_pix_corrigido.csv'

# Carregar o arquivo CSV para um DataFrame do pandas
df = pd.read_csv(arquivo_entrada)

# Converter o campo 'valor' para string e substituir o ponto por vírgula
df['valor'] = df['valor'].astype(str).str.replace('.', ',')

# Salvar o DataFrame de volta para um novo arquivo CSV com os valores corrigidos
df.to_csv(arquivo_saida, index=False)

print(f'Arquivo corrigido salvo em: {arquivo_saida}')

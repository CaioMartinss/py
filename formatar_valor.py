import pandas as pd

# Carregar o arquivo CSV ordenado
df = pd.read_csv('./transacoes_pix_ordenado.csv')

# Formatar a coluna 'valor' como moeda
df['valor'] = df['valor'].apply(lambda x: f"R${x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Salvar o DataFrame em um novo arquivo CSV
df.to_csv('transacoes_pix_gsheets.csv', index=False)

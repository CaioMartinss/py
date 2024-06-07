import pandas as pd

import pandas as pd

# Passo 1: Ler o arquivo CSV
arquivo_csv = 'transacoes_pix.csv'
df = pd.read_csv(arquivo_csv)

# Passo 2: Converter a coluna 'valor' para string e aplicar a formatação de moeda
df['valor'] = df['valor'].apply(lambda x: '{:,.2f}'.format(x).replace(',', 'v').replace('.', ',').replace('v', '.'))

# Exibir ou salvar o resultado
print(df)

# Salvar em um novo arquivo CSV com o estilo brasileiro

arquivo_csv_formatado = 'transacoes_pix_formatado_virgula.csv'
df.to_csv(arquivo_csv_formatado, index=False, sep=';', decimal=',')
print(f'Dados salvos em {arquivo_csv_formatado}')




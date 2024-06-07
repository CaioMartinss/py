import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV fornecido pelo usuário
df = pd.read_csv('transacoes_origem_destino_repetidas.csv')

# Filtrar transações que se repetem a partir de 11 vezes e remover 'Desconhecido'
df_filtrado = df[(df['vezes_que_repetiu'] >= 11) & (df['ano'].notnull())]

# Converter o ano para string
df_filtrado['ano'] = df_filtrado['ano'].astype(int).astype(str)

# Agrupar por origem, destino e ano, contando as repetições
df_agrupado = df_filtrado.groupby(['origem', 'destino', 'ano']).agg(
    vezes_que_repetiu=('vezes_que_repetiu', 'sum')
).reset_index()

# Ordenar novamente por contagem de repetições
df_agrupado = df_agrupado.sort_values(by='vezes_que_repetiu', ascending=False)

# Preparar os dados para o gráfico
# Criar uma coluna com a combinação de origem e destino formatada
df_agrupado['origem_destino'] = df_agrupado['origem'] + ' -> ' + df_agrupado['destino']

# Configurar o tamanho do gráfico
plt.figure(figsize=(12, 8))

# Cores para cada ano
cores = {'2021': 'skyblue', '2022': 'salmon'}

# Plotar o gráfico de barras agrupado por ano
for ano, dados in df_agrupado.groupby('ano'):
    plt.barh(dados['origem_destino'], dados['vezes_que_repetiu'], color=cores[ano], label=ano)

plt.xlabel('Número de Repetições')
plt.ylabel('Origem -> Destino')
plt.title('Transações mais Recorrentes por Ano (11 ou mais repetições)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Exibir o gráfico
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV
file_path = './analise_dados_py.csv'
df = pd.read_csv(file_path)

# Verificar as colunas do DataFrame
print(df.columns)

# Estatísticas Descritivas
mean_value = df['valor_total_dia'].str.replace('.', '').str.replace(',', '.').astype(float).mean()
median_value = df['valor_total_dia'].str.replace('.', '').str.replace(',', '.').astype(float).median()
std_deviation = df['valor_total_dia'].str.replace('.', '').str.replace(',', '.').astype(float).std()
total_transacoes = df['total_transacoes'].sum()
volume_total_transacionado = df['volume_total_transicionado'].str.replace('.', '').str.replace(',', '.').astype(float).sum()

print(f"Média: {mean_value}")
print(f"Mediana: {median_value}")
print(f"Desvio Padrão: {std_deviation}")
print(f"Total de Transações: {total_transacoes}")
print(f"Volume Total Transacionado: {volume_total_transacionado}")

# Visualizações Iniciais
# Histograma
plt.figure(figsize=(10, 6))
sns.histplot(df['valor_total_dia'].str.replace('.', '').str.replace(',', '.').astype(float), bins=30, kde=True)
plt.title('Histograma do Valor Total por Dia')
plt.xlabel('Valor Total por Dia')
plt.ylabel('Frequência')
plt.show()

# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['valor_total_dia'].str.replace('.', '').str.replace(',', '.').astype(float))
plt.title('Boxplot do Valor Total por Dia')
plt.xlabel('Valor Total por Dia')
plt.show()

# Scatter Plot (Exemplo de relação entre valor da transação e algum outro parâmetro, como data)
plt.figure(figsize=(10, 6))
sns.scatterplot(x=pd.to_datetime(df['dia']), y=df['valor_total_dia'].str.replace('.', '').str.replace(',', '.').astype(float))
plt.title('Scatter Plot do Valor Total das Transações ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Valor Total por Dia')
plt.xticks(rotation=45)
plt.show()

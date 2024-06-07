import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV gerado anteriormente
df = pd.read_csv('transacoes_pix.csv')

# Calcular estatísticas descritivas
media_valor = df['valor'].mean()
mediana_valor = df['valor'].median()
desvio_padrao_valor = df['valor'].std()
total_transacoes = df.shape[0]
volume_total_transacionado = df['valor'].sum()

# Imprimir as estatísticas
print(f"Estatísticas Descritivas:")
print(f"  Média do valor das transações: R${media_valor:.2f}")
print(f"  Mediana do valor das transações: R${mediana_valor:.2f}")
print(f"  Desvio padrão do valor das transações: R${desvio_padrao_valor:.2f}")
print(f"  Total de transações: {total_transacoes}")
print(f"  Volume total transacionado: R${volume_total_transacionado:.2f}")

# Histograma
plt.figure(figsize=(12, 6))
plt.hist(df['valor'], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribuição dos Valores das Transações', fontsize=15)
plt.xlabel('Valor das Transações (R$)', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

# Boxplot
plt.figure(figsize=(10, 6))
boxprops = dict(linewidth=2, color='darkblue')
medianprops = dict(linewidth=2, color='orange')
plt.boxplot([df[df['tipo_transacao'] == 'pessoal']['valor'],
             df[df['tipo_transacao'] == 'empresarial']['valor']],
            labels=['Pessoal', 'Empresarial'],
            boxprops=boxprops,
            medianprops=medianprops)
plt.title('Distribuição dos Valores das Transações por Tipo', fontsize=15)
plt.ylabel('Valor das Transações (R$)', fontsize=12)
plt.xlabel('Tipo de Transação', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

# Scatter plot
plt.figure(figsize=(12, 6))
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
plt.scatter(df['data'], df['valor'], alpha=0.5, color='green')
plt.title('Valor das Transações ao Longo do Tempo', fontsize=15)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Valor das Transações (R$)', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

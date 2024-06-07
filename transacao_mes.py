import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados das métricas descritivas
metricas_empresarial = pd.read_csv('metricas_transacoes_empresariais.csv')
metricas_pessoal = pd.read_csv('metricas_transacoes_pessoais.csv')

# Convertendo a coluna 'dia' para datetime
metricas_empresarial['dia'] = pd.to_datetime(metricas_empresarial['dia'])
metricas_pessoal['dia'] = pd.to_datetime(metricas_pessoal['dia'])

# Extrair ano e mês para cada tipo
metricas_empresarial['ano'] = metricas_empresarial['dia'].dt.year
metricas_empresarial['mes'] = metricas_empresarial['dia'].dt.month

metricas_pessoal['ano'] = metricas_pessoal['dia'].dt.year
metricas_pessoal['mes'] = metricas_pessoal['dia'].dt.month

# Calcular a quantidade de transações por mês de cada tipo por ano
transacoes_empresarial_por_mes_ano = metricas_empresarial.groupby(['ano', 'mes'])['total_transacoes_mes'].sum().reset_index()
transacoes_pessoal_por_mes_ano = metricas_pessoal.groupby(['ano', 'mes'])['total_transacoes_mes'].sum().reset_index()

# Renomear os meses para exibição nos gráficos
meses_pt = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

# Verificar os anos disponíveis nos dados
print("Anos disponíveis para Empresarial:", transacoes_empresarial_por_mes_ano['ano'].unique())
print("Anos disponíveis para Pessoal:", transacoes_pessoal_por_mes_ano['ano'].unique())

# Ajuste das cores para garantir visibilidade do ano de 2021
empresarial_palette = {2021: 'lightblue', 2022: 'darkblue'}
pessoal_palette = {2021: 'lightgreen', 2022: 'darkgreen'}

# Criar gráficos para visualizar os dados

# Histograma de quantidade de transações mensais por ano (empresarial e pessoal)
plt.figure(figsize=(14, 6))

# Empresarial
plt.subplot(1, 2, 1)
sns.barplot(data=transacoes_empresarial_por_mes_ano, x='mes', y='total_transacoes_mes', hue='ano', palette=empresarial_palette)
plt.title('Quantidade de Transações Mensais (Empresarial)')
plt.xlabel('Mês')
plt.ylabel('Quantidade de Transações')
plt.xticks(ticks=range(1, 13), labels=meses_pt)
plt.legend(title='Ano')

# Pessoal
plt.subplot(1, 2, 2)
sns.barplot(data=transacoes_pessoal_por_mes_ano, x='mes', y='total_transacoes_mes', hue='ano', palette=pessoal_palette)
plt.title('Quantidade de Transações Mensais (Pessoal)')
plt.xlabel('Mês')
plt.ylabel('Quantidade de Transações')
plt.xticks(ticks=range(1, 13), labels=meses_pt)
plt.legend(title='Ano')

plt.tight_layout()
plt.show()

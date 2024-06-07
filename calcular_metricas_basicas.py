import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados das métricas descritivas
metricas_empresarial = pd.read_csv('metricas_transacoes_empresariais.csv')
metricas_pessoal = pd.read_csv('metricas_transacoes_pessoais.csv')

# Convertendo a coluna 'dia' para datetime
metricas_empresarial['dia'] = pd.to_datetime(metricas_empresarial['dia'])
metricas_pessoal['dia'] = pd.to_datetime(metricas_pessoal['dia'])

# Extrair o ano para cada conjunto de dados
metricas_empresarial['ano'] = metricas_empresarial['dia'].dt.year
metricas_pessoal['ano'] = metricas_pessoal['dia'].dt.year

# Agrupar os dados por ano e mês, somando os valores totais
metricas_empresarial_ano_mes = metricas_empresarial.groupby([metricas_empresarial['ano'], metricas_empresarial['dia'].dt.month])['valor_total_mes'].sum().reset_index()
metricas_pessoal_ano_mes = metricas_pessoal.groupby([metricas_pessoal['ano'], metricas_pessoal['dia'].dt.month])['valor_total_mes'].sum().reset_index()

# Renomeando os meses para siglas em português
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

# Definindo a paleta de cores baseada nos anos disponíveis
paleta_empresarial = sns.color_palette("Blues", n_colors=len(metricas_empresarial_ano_mes['ano'].unique()))
paleta_pessoal = sns.color_palette("Greens", n_colors=len(metricas_pessoal_ano_mes['ano'].unique()))

# Histograma de volume total transacionado por mês e ano (empresarial e pessoal)
plt.figure(figsize=(14, 6))

# Empresarial
plt.subplot(1, 2, 1)
sns.barplot(data=metricas_empresarial_ano_mes, x='dia', y='valor_total_mes', hue='ano', palette=paleta_empresarial, alpha=1)
plt.title('Volume Total Transacionado Mensalmente por Ano (Empresarial)')
plt.xlabel('Mês')
plt.ylabel('Volume Total Transacionado')
plt.xticks(ticks=range(12), labels=meses)
plt.legend(title='Ano')

# Pessoal
plt.subplot(1, 2, 2)
sns.barplot(data=metricas_pessoal_ano_mes, x='dia', y='valor_total_mes', hue='ano', palette=paleta_pessoal, alpha=1)
plt.title('Volume Total Transacionado Mensalmente por Ano (Pessoal)')
plt.xlabel('Mês')
plt.ylabel('Volume Total Transacionado')
plt.xticks(ticks=range(12), labels=meses)
plt.legend(title='Ano')

plt.tight_layout()
plt.show()

# Gráfico comparativo mensal (mantido sem alterações)
plt.figure(figsize=(10, 6))
plt.plot(meses, metricas_empresarial_ano_mes[metricas_empresarial_ano_mes['ano'] == metricas_empresarial_ano_mes['ano'].max()]['valor_total_mes'], marker='o', label='Empresarial', color='blue')
plt.plot(meses, metricas_pessoal_ano_mes[metricas_pessoal_ano_mes['ano'] == metricas_pessoal_ano_mes['ano'].max()]['valor_total_mes'], marker='o', label='Pessoal', color='green')
plt.title('Valores Totais Transacionados Mensalmente (Último Ano Disponível)')
plt.xlabel('Mês')
plt.ylabel('Valor Total Transacionado')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

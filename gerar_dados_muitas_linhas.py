import pandas as pd
import random
from faker import Faker
from tqdm import tqdm
from datetime import datetime

# Configurar o Faker para gerar dados fictícios
fake = Faker('pt_BR')

# Configurações
num_transacoes = 200000
start_date = datetime.strptime('2021-01-01', '%Y-%m-%d').date()
end_date = datetime.strptime('2023-01-01', '%Y-%m-%d').date()

# Função para gerar tipo de transação e valor
def generate_transaction():
  if random.random() < 0.7:  # 70% das transações são pessoais
    tipo_transacao = 'pessoal'
    valor = round(random.uniform(10, 3000), 2)  # Valores entre 10 e 3.000
  else:  # 30% das transações são empresariais
    tipo_transacao = 'empresarial'
    valor = round(random.uniform(3000, 100000), 2)  # Valores entre 3.000 e 100.000
  return tipo_transacao, valor

# Gerar dados fictícios
data = []
for _ in tqdm(range(num_transacoes), desc="Gerando transações"):
  date = fake.date_between(start_date=start_date, end_date=end_date).strftime('%d/%m/%Y')
  hora = fake.time()
  origem = fake.city()
  destino = fake.city()
  tipo_transacao, valor = generate_transaction()
  mes_ano = f"{date[3:5]}.{date[6:]}"
  data.append([date, valor, hora, origem, destino, tipo_transacao, mes_ano])

# Criar DataFrame
df = pd.DataFrame(data, columns=['data', 'valor', 'hora', 'origem', 'destino', 'tipo_transacao', 'mes_ano'])

# Ordenar por data
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
df = df.sort_values('data').reset_index(drop=True)
df['data'] = df['data'].dt.strftime('%d/%m/%Y')

# Salvar em CSV
output_path = 'transacoes_pix.csv'
df.to_csv(output_path, index=False)

print(f"Arquivo CSV salvo em: {output_path}")

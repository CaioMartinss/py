import pandas as pd
import numpy as np
import random
from datetime import datetime

# Lista de capitais do Brasil
capitais = [
    'Aracaju', 'Belém', 'Belo Horizonte', 'Boa Vista', 'Brasília', 'Campo Grande', 'Cuiabá',
    'Curitiba', 'Florianópolis', 'Fortaleza', 'Goiânia', 'João Pessoa', 'Macapá', 'Maceió',
    'Manaus', 'Natal', 'Palmas', 'Porto Alegre', 'Porto Velho', 'Recife', 'Rio Branco',
    'Rio de Janeiro', 'Salvador', 'São Luís', 'São Paulo', 'Teresina', 'Vitória'
]

# Função para gerar dados
def generate_data(num_rows):
    data = []
    for _ in range(num_rows):
        if random.random() < 0.1:  # 10% chance de ser fevereiro
            mes = 'fev_2023'
        else:
            mes = random.choice(['jan_2023', 'mar_2023', 'abr_2023', 'mai_2023', 'jun_2023', 'jul_2023', 'ago_2023', 'set_2023', 'out_2023', 'nov_2023', 'dez_2023'])
        
        hora = random.randint(0, 23)
        tipo_transacao = random.choice(['pessoal', 'empresarial'])
        
        if tipo_transacao == 'pessoal':
            valor_transacao = f'R$ {round(random.uniform(10, 20000), 2):,.2f}'  # Intervalo para transações pessoais: entre R$ 10 e R$ 20.000
        else:
            valor_transacao = f'R$ {round(random.uniform(1000, 100000), 2):,.2f}'  # Intervalo para transações empresariais: entre R$ 1.000 e R$ 100.000
        
        # Gerar mais transações para Salvador e Rio de Janeiro
        if mes == 'fev_2023' and random.random() < 0.5:
            origem = random.choice(['Salvador', 'Rio de Janeiro'])
        else:
            origem = random.choice(capitais)
        
        destino = random.choice(capitais)
        while destino == origem:
            destino = random.choice(capitais)
        
        data.append([valor_transacao, mes, hora, tipo_transacao, origem, destino])
    
    return data

# Gerar dados
num_rows = 10000
data = generate_data(num_rows)

# Criar DataFrame
df = pd.DataFrame(data, columns=['valor_transacao', 'data', 'hora', 'tipo_transacao', 'origem', 'destino'])

# Salvar em um arquivo CSV
df.to_csv('transacoes_capitais.csv', index=False)

# Mostrar uma amostra dos dados
print(df.head())

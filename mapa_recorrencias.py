import pandas as pd
import folium
from folium.plugins import HeatMap
import io

# Coordenadas das cidades reais e fictícias
cidades_coordenadas = {
    'da Rocha': (-23.5505, -46.6333),  # São Paulo
    'Sá': (-22.9068, -43.1729),  # Rio de Janeiro
    'da Mota': (-20.3155, -40.3128),  # Brasília
    'Oliveira': (-12.9714, -38.5014),  # Belo Horizonte
    'Viana': (-3.119, -60.0217),  # Manaus
    'Peixoto': (-5.79447, -35.211),  # Natal
    'Cavalcanti': (-8.0476, -34.877),  # Recife
    'das Neves': (-19.9187, -43.9388),  # Belo Horizonte
    'Brito': (-3.7172, -38.5433),  # Manaus
    'Silveira': (-22.9068, -43.1729),  # Rio de Janeiro (Usando a mesma de 'Sá')
    'Campos': (-22.9068, -43.1729),  # Rio de Janeiro (Usando a mesma de 'Sá')
    'Montenegro': (-8.0476, -34.877),  # Recife (Usando a mesma de 'Cavalcanti')
    'da Paz': (-8.0476, -34.877),  # Recife (Usando a mesma de 'Cavalcanti')
    # Adicione mais cidades conforme necessário
}

# Dados das transações
dados = """
origem,destino,vezes_que_repetiu,ano
da Rocha,Sá,14,2022.0
da Mota,Oliveira,14,
Viana,Peixoto,14,2022.0
Cavalcanti,das Neves,13,2021.0
Sá,Brito,13,
Aparecida,Silveira,13,
Rezende,Campos,13,2022.0
Rezende,Silva,12,2022.0
Camargo,da Conceição,12,
Câmara,Machado,12,2021.0
Moraes,Novais,12,
Leão,Pinto,12,
Camargo,Pinto,12,
Sousa,Correia,12,2022.0
das Neves,da Mata,12,2022.0
Barbosa,Lopes,12,
das Neves,Moura,12,2022.0
da Paz,Campos,12,
Rezende,Cardoso,12,2022.0
da Rosa,Moraes,12,2022.0
Freitas,Nascimento,12,
Araújo,Oliveira,12,2021.0
Carvalho,Viana,11,2021.0
Macedo,Rios,11,2021.0
Machado,Duarte,11,2021.0
da Rosa,Barbosa,11,2022.0
Cirino,Montenegro,11,2021.0
das Neves,Fogaça,11,2022.0
Souza,Montenegro,11,2022.0
Barbosa,Abreu,11,
Casa Grande,Campos,11,2021.0
Pinto,Araújo,11,2022.0
Vasconcelos,Jesus,11,
Martins,Rodrigues,11,
Martins,da Paz,11,
Vasconcelos,Porto,11,2022.0
das Neves,Cavalcanti,11,2022.0
Gomes,Vieira,11,
Novaes,Porto,11,
Leão,Albuquerque,11,
Câmara,Pinto,11,2021.0
Guerra,Souza,11,2021.0
Sá,Rocha,11,
Guerra,das Neves,11,2021.0
Cunha,Nogueira,11,
Dias,Dias,11,2021.0
Pacheco,Campos,11,
Pimenta,Freitas,11,2022.0
Sá,Moreira,11,
Gomes,Fernandes,11,
Pimenta,Casa Grande,11,2022.0
Gonçalves,Gonçalves,11,2021.0
Dias,Pimenta,11,2021.0
Duarte,Aragão,11,
Sales,Siqueira,11,2022.0
Sales,Mendes,11,2022.0
Freitas,Pimenta,11,
Borges,Rezende,11,2021.0
Vasconcelos,Rezende,11,2022.0
Câmara,Monteiro,11,2021.0
Pereira,Pastor,11,
Aparecida,Silva,11,
Freitas,Gonçalves,11,
Aragão,Alves,11,2021.0
Viana,Martins,11,2022.0
Nunes,Vieira,11,2021.0
da Paz,Costa,11,
Mendonça,Sousa,11,2021.0
Cassiano,Moraes,11,
Andrade,Porto,11,
Brito,Pires,11,2021.0
Ribeiro,Cirino,11,2022.0
Monteiro,Nogueira,11,
Moraes,Cavalcante,11,
Rezende,Fernandes,11,2022.0
Abreu,Barbosa,11,2021.0
Pinto,Fonseca,11,2022.0
da Cruz,da Rocha,11,
Aragão,Camargo,11,2021.0
Fonseca,Vasconcelos,11,2021.0
Moreira,Mendes,11,
Moreira,Castro,11,
Souza,Cassiano,11,2022.0
Araújo,Aparecida,11,2021.0
Casa Grande,Pires,11,2021.0
Mendes,Ramos,11,2021.0
Pereira,Mendonça,11,
Rios,Nunes,11,
Aragão,Moura,11,2021.0
Vasconcelos,Vieira,11,2022.0
Pastor,da Mota,11,
Melo,Teixeira,11,
"""

# Carregar os dados como um DataFrame
df = pd.read_csv(io.StringIO(dados))

# Filtrar transações que se repetem a partir de 11 vezes e remover 'Desconhecido'
df_filtrado = df[(df['vezes_que_repetiu'] >= 11) & (df['ano'].notnull())]

# Converter o ano para string
df_filtrado['ano'] = df_filtrado['ano'].astype(int).astype(str)

# Verificar quais cidades não foram encontradas
cidades_nao_encontradas = set()
for cidade in df_filtrado['origem'].unique():
    if cidade not in cidades_coordenadas:
        cidades_nao_encontradas.add(cidade)
for cidade in df_filtrado['destino'].unique():
    if cidade not in cidades_coordenadas:
        cidades_nao_encontradas.add(cidade)

print(f"Cidades não encontradas: {cidades_nao_encontradas}")

# Mapear as cidades fictícias para cidades reais se necessário
for cidade in cidades_nao_encontradas:
    cidades_coordenadas[cidade] = (-15.788, -47.8797)  # Coordenadas de Brasília como padrão

df_filtrado['origem'] = df_filtrado['origem'].apply(lambda x: cidades_coordenadas[x] if x in cidades_coordenadas else cidades_coordenadas[next(iter(cidades_coordenadas))])
df_filtrado['destino'] = df_filtrado['destino'].apply(lambda x: cidades_coordenadas[x] if x in cidades_coordenadas else cidades_coordenadas[next(iter(cidades_coordenadas))])

# Preparar os dados para o mapa de calor
heat_data = []
for index, row in df_filtrado.iterrows():
    origem = row['origem']
    destino = row['destino']
    vezes_que_repetiu = row['vezes_que_repetiu']
    heat_data.append(list(origem) + [vezes_que_repetiu])
    heat_data.append(list(destino) + [vezes_que_repetiu])

# Criar um mapa inicial com base nas coordenadas médias
mapa = folium.Map(location=[-15.788, -47.8797], zoom_start=4)

# Adicionar o mapa de calor com base nos dados preparados
HeatMap(heat_data).add_to(mapa)

# Adicionar marcadores para cada cidade com base nas coordenadas
for cidade, coordenadas in cidades_coordenadas.items():
    folium.Marker(location=coordenadas, popup=cidade).add_to(mapa)

# Salvar o mapa como um arquivo HTML
mapa.save("mapa_recorrencias.html")

print("Mapa de calor salvo como 'mapa_recorrencias.html'.")

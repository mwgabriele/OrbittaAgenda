import requests
from bs4 import BeautifulSoup
import sqlite3
from control import missao

#
# raspagem de missões do site space launch
#
url = 'https://www.spacelaunchschedule.com/category/spacex/'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(response.text, 'html.parser')

titulos = soup.find_all('h2', class_='entry-title h4 font-weight-bold')
veiculos = soup.find_all('span', class_='h5 mt-2 d-block')
agencias = soup.find_all('h3', class_='h6 mb-3')
locais = soup.find_all('div', class_='col h6 mb-0 pt-2')
resultados = soup.find_all('div', class_='col h6 mb-1 pt-1 text-uppercase')

conexao = sqlite3.connect('missoes.db')
cursor = conexao.cursor()

for titulo in titulos:
    nome_missao = titulo.get_text(strip=True)
    if nome_missao:
        print(nome_missao)
        cursor.execute("INSERT INTO lancamentos_espaciais (nome_missao) VALUES (?)", (nome_missao,))

for veiculo in veiculos:
    veiculo_lancador = veiculo.get_text(strip=True)
    if veiculo_lancador:
        print(veiculo_lancador)
        cursor.execute("INSERT INTO lancamentos_espaciais (veiculo_lancador) VALUES (?)", (veiculo_lancador,))

for agencia in agencias:
    nome_agencia = agencia.get_text(strip=True)
    if nome_agencia:
        print(nome_agencia)
        cursor.execute("INSERT INTO lancamentos_espaciais (nome_agencia) VALUES (?)", (nome_agencia,))

for local in locais:
    local_lancamento = local.get_text(strip=True)
    if local_lancamento:
        print(local_lancamento)
        cursor.execute("INSERT INTO lancamentos_espaciais (local_lancamento) VALUES (?)", (local_lancamento,))

for result in resultados:
    resultado = result.get_text(strip=True)
    if resultado:
        print(resultado)
        cursor.execute("INSERT INTO lancamentos_espaciais (resultado) VALUES (?)", (resultado,))

conexao.commit()
conexao.close()
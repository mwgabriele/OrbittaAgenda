import requests
from bs4 import BeautifulSoup
import sqlite3

#
# raspagem de missões do site da ESA
#
url = 'https://www.esa.int/ESA/Our_Missions/(sort)/date'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(response.text, 'html.parser')

titulos = soup.find_all('h3', class_='heading')

conexao = sqlite3.connect('missoes.db')
cursor = conexao.cursor()

for titulo in titulos:
    nome_missao = titulo.get_text(strip=True)
    if nome_missao:
        print(nome_missao)
        cursor.execute("INSERT INTO lancamentos_espaciais (nome_missao) VALUES (?)", (nome_missao,))

conexao.commit()
conexao.close()
import requests
from bs4 import BeautifulSoup
import sqlite3

#
# raspagem de missões do site Spaceflight Now
#
url = 'https://spaceflightnow.com/launch-schedule/'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(response.text, 'html.parser')

titulos = soup.find_all('span', class_='mission')

conexao = sqlite3.connect('missoes.db')
cursor = conexao.cursor()

for titulo in titulos:
    nome_missao = titulo.get_text(strip=True)
    if nome_missao:
        print(nome_missao)
        cursor.execute("INSERT INTO lancamentos_espaciais (nome_missao) VALUES (?)", (nome_missao,))

conexao.commit()
conexao.close()
import requests
from bs4 import BeautifulSoup
import sqlite3

#
# raspagem das missoes da nasa de A-Z do site da Nasa
#
url = 'https://www.nasa.gov/a-to-z-of-nasa-missions/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# pegando só os links da lista de missões
titulos = soup.select("p > a")

# conectando ao banco
conexao = sqlite3.connect("missoes.db")
cursor = conexao.cursor()

# garantindo que a tabela existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS lancamentos_espaciais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_missao TEXT
)
""")

# extraindo e inserindo no banco
for titulo in titulos:
    nome_missao = titulo.get_text(strip=True)
    if nome_missao:
        print(nome_missao)
        cursor.execute("INSERT INTO lancamentos_espaciais (nome_missao) VALUES (?)", (nome_missao,))

conexao.commit()
conexao.close()
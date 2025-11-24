import sqlite3

sql_create_table_eventos_astronomicos = '''
CREATE TABLE IF NOT EXISTS eventos_astronomicos (
    id INTEGER PRIMARY KEY NOT NULL,
    nome_evento TEXT,
    tipo_evento TEXT,
    descricao TEXT,
    data TEXT,
    horario_utc3 TEXT,
    local_visivel TEXT,
    duracao TEXT,
    corpo_principal TEXT,
    frequencia TEXT,
    observacao_comum TEXT
);
'''
sql_create_table_lancamentos_espaciais = '''
CREATE TABLE IF NOT EXISTS lancamentos_espaciais (
    id INTEGER PRIMARY KEY NOT NULL,
    nome_missao TEXT,
    veiculo_lancador TEXT,
    nome_agencia TEXT,
    carga TEXT,
    destino TEXT,
    data TEXT,
    horario_utc3 TEXT,
    local_lancamento TEXT,
    resultado TEXT,
    descricao TEXT
);
'''
sql_create_table_agencias = '''
CREATE TABLE IF NOT EXISTS agencias (
    id INTEGER PRIMARY KEY NOT NULL,
    nome_agencia TEXT,
    pais TEXT
);
'''

sql_inserir_dados_eventos_astronomicos = '''
INSERT INTO eventos_astronomicos (nome_evento, tipo_evento, descricao, data, horario, local_visivel, duracao, corpo_principal, frequencia, observacao_comum)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
'''
sql_inserir_dados_lancamentos_espaciais = '''
INSERT INTO lancamentos_espaciais (nome_missao, veiculo_lancador, nome_agencia, carga, destino, data, horario_utc3, local_lancamento, resultado, descricao)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
sql_inserir_dados_agencias = '''
INSERT INTO agencias (nome_agencia, pais)
VALUES (?, ?)
'''

sql_delete_query = '''
DELETE FROM lancamentos_espaciais
WHERE nome_missao = ?;
'''



with sqlite3.connect("missoes.db") as conexao:
    conexao.execute(sql_create_table_eventos_astronomicos)
    conexao.execute(sql_create_table_lancamentos_espaciais)
    conexao.execute(sql_create_table_agencias)

    conexao.commit()

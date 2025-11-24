# Projeto Orbitta Agenda
## Eventos da astronomia e astronáutica -> Banco de Dados
O Orbitta:
Banco de dados SQLite. Tabelas:

### Eventos astronômicos

- id
- nome_evento
- tipo_evento
- descricao
- data
- horario_utc3 (UTC-3)
- local_visivel (onde poderá ser observado -> a definir! ex.: América do Sul, apenas Hemisfério Norte...)
- duracao (se aplicável. Eclipse, chuva de meteóro, etc...)
- corpo_principal
- frequencia
- observacao_popular/comum (?) (visível a olho nu, binóculo, telescópio...)

### Lançamentos espaciais

- id
- nome_missao (ex.: Apollo)
- veiculo_lancador (ex.: Saturn V)
- nome_agencia
- carga (ex.: satélite, sonda, telescópio, tripulação)
- destino
- data
- horario_utc3
- local_lancamento
- resultado (sucesso, falha, adiado)
- descricao

### Agências

- id
- nome_agencia
- pais
- Objetos -> Missao: -> Evento: ->

Ordem de páginas usadas no preenchimento de nome_missao do banco:

nasa
spaceflight now
roscosmos
everyday astronaut
supercluster
etapas: raspagem de dados da web; interface gráfica para a consulta
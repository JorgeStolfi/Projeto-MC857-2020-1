import trecho
import poltrona
import html_texto

def gera(obj_trecho):
  id_trecho = trecho.obtem_identificador(obj_trecho)
  atrs_trecho = trecho.obtem_atributos(obj_trecho)

  # em 22/05 isso estava com erro, então coloquei dentro do try
  try:
      ids_poltronas = poltrona.busca_por_trecho(obj_trecho)
  except:
      ids_poltronas = []

  # atributos trecho
  codigo = atrs_trecho['codigo']
  origem = atrs_trecho['origem']
  destino = atrs_trecho['destino']
  dt_partida = atrs_trecho['dia_partida'] + " " + atrs_trecho['hora_partida']
  dt_chegada = atrs_trecho['dia_chegada'] + " " + atrs_trecho['hora_chegada']
  num_poltronas = str(len(ids_poltronas))

  # blocos de texto para tabela
  ht_codigo = ('Código', html_texto.gera(codigo, None, None, None, None, None, None, None, None))
  ht_origem = ('Origem', html_texto.gera(origem, None, None, None, None, None, None, None, None))
  ht_destino = ('Destino', html_texto.gera(destino, None, None, None, None, None, None, None, None))
  ht_dt_partida = ('Data de Partida', html_texto.gera(dt_partida, None, None, None, None, None, None, None, None))
  ht_dt_chegada = ('Data de Chegada', html_texto.gera(dt_chegada, None, None, None, None, None, None, None, None))
  ht_num_poltronas = ('Número de Poltronas', html_texto.gera(num_poltronas, None, None, None, None, None, None, None, None))

  ht_campos = (ht_codigo, ht_origem, ht_destino, ht_dt_partida, ht_dt_chegada, ht_num_poltronas)

  return ht_campos

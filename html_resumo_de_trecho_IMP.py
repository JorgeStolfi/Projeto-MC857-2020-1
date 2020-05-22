import trecho
import poltrona
import html_texto

def gera(trc):
  id_trecho = trecho.obtem_identificador(trc)
  atrs_trecho = trecho.obtem_atributos(trc)
  ids_poltronas = poltrona.busca_por_trecho(trc)
  # atributos trecho
  codigo = atrs_trecho['codigo']
  origem = atrs_trecho['origem']
  destino = atrs_trecho['destino']
  dt_partida = atrs_trecho['dia_partida'] + " " + atrs_trecho['hora_partida']
  dt_chegada = atrs_trecho['dia_chegada'] + " " + atrs_trecho['hora_chegada']
  num_poltronas = len(ids_poltronas)
  
  # blocos de texto para tabela
  ht_codigo = html_texto.gera(codigo, None, None, None, None, None, None, None, None)
  ht_origem = html_texto.gera(origem, None, None, None, None, None, None, None, None)
  ht_destino = html_texto.gera(destino, None, None, None, None, None, None, None, None)
  ht_dt_partida = html_texto.gera(dt_partida, None, None, None, None, None, None, None, None)
  ht_dt_chegada = html_texto.gera(dt_chegada, None, None, None, None, None, None, None, None)
  ht_num_poltronas = html_texto.gera(str(num_poltronas), None, None, None, None, None, None, None, None)
  ht_campos = ( ht_codigo, ht_origem, ht_destino, ht_dt_partida, ht_dt_chegada, ht_num_poltronas )
  return ht_campos

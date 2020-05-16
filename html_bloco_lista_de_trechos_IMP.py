
import trecho
import html_bloco_texto
import html_tabela

def gera(ses, ids):
  linhas = [].copy()
  for id_trecho in ids:
    trecho1 = trecho.busca_por_identificador(id_trecho)
    atrs_trecho = trecho.obtem_atributos(trecho1)
    # atributos trecho
    codigo = atrs_trecho['codigo']
    origem = atrs_trecho['origem']
    destino = atrs_trecho['destino']
    dt_partida = atrs_trecho['dt_partida']
    dt_chegada = atrs_trecho['dt_chegada']
    # blocos de texto para tabela
    ht_codigo = html_bloco_texto.gera(codigo, None, None, None, None, None, None, None, None)
    ht_origem = html_bloco_texto.gera(origem, None, None, None, None, None, None, None, None)
    ht_destino = html_bloco_texto.gera(destino, None, None, None, None, None, None, None, None)
    ht_dt_partida = html_bloco_texto.gera(dt_partida, None, None, None, None, None, None, None, None)
    ht_dt_chegada = html_bloco_texto.gera(dt_chegada, None, None, None, None, None, None, None, None)
    # linhas da tabela
    linhas.append(( ht_codigo, ht_origem, ht_destino, ht_dt_partida, ht_dt_chegada ))
  # tabela
  ht_itens = html_tabela.gera(linhas)
  return ht_itens

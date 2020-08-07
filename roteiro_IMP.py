import trecho
from utils_testes import erro_prog
import sys
import re

def descobre_todos_rec(origem, data_min, prefixo, destino, data_max, soh_disponiveis):
  """Função auxiliar da função {descobre_todos}.

  O parâmetro {prefixo} é o roteiro parcial que atualmente esta sendo montado.
  Se não for uma lista vazia, deve ser um roteiro válido que começa
  em {origem}, não antes de {data_min}.
  
  A função calcula recursivamente todos as extensões válidas do
  {prefixo} que saem do aeroporto onde este termina e terminam em
  {destino}, e devolve uma lista de todos esses roteiros.
  
  Para ser válido, um roteiro não pode terminar depois de {data_max}, 
  e cada trecho além do primeiro deve sair do mesmo aeroporto onde o trecho
  anterior chegou, com intervalo de tempo suficiente para a baldeação. 
  
  As datas devem ter o formato "aaaa-mm-dd HH:MM UTC".

  """
  
  debug = True
  
  # Pega o último trecho do prefixo:
  trc_prev = None if len(prefixo) == 0 else prefixo[-1];
  if debug:
    sys.stderr.write("  " * len(prefixo))
    sys.stderr.write("trc_prev = %s\n" % trecho.mostra(trc_prev))
  assert (trc_prev == None) or (type(trc_prev) is trecho.Objeto_Trecho)

  # Pega o aeroporto final do {prefixo}
  etapa = origem if trc_prev == None else trecho.obtem_atributo(trc_prev, 'destino')
  if etapa == destino: 
    #  Este prefixo é uma slução e não adianta tentar estendê-lo:
    return [ prefixo ]
  
  rots = [].copy() # Os roteiros encontrados que começam com {prefixo}.
  
  # Pega todos os trechos que saem de {etapa}:
  for id_trc_prox in trecho.busca_por_origem(etapa):
  
    trc_prox = trecho.busca_por_identificador(id_trc_prox)
    assert trc_prox != None # Paranóia.
    
    # Verifica tempo. Este é o teste que impede recursão infinita.
    if trc_prev != None:
      # Verifica se há tempo suficiente para a baldeação:
      dt_sai_ok = trecho.horarios_sao_compativeis(trc_prev, trc_prox)
    else:
      # Verifica se {trc_prox} não sai antes da data mínima de partide:
      data_sai = trecho.obtem_dia_e_hora_de_chegada(trc_prox)
      dt_sai_ok = (data_sai >= data_min)
    if not dt_sai_ok: continue
    
    if soh_disponiveis:
      # Verifica se este trecho está não encerrado para compra:
      disp = trecho.verificar_disponibilidade(trc_prox)
      if not disp: continue
    
    # Verifica se este trecho termina antes da data limite:
    data_chg = trecho.obtem_dia_e_hora_de_partida(trc_prox)
    data_chg_ok = (data_chg <= data_max)
    if not data_chg_ok: continue

    # Emenda este trecho no prefixo e busca recursivamente:
    prefixo1 = prefixo + [ trc_prox ]
    rots1 = descobre_todos_rec(origem, data_min, prefixo1, destino, data_max, soh_disponiveis)
    rots += rots1

  # Esgotou todas as possiveis extensoes do {prefixo}:
  return rots
  
def descobre_todos(origem, data_min, destino, data_max, soh_disponiveis):

  # Verifica formato das datase outras consistências:
  assert re.fullmatch(r'20[0-9][0-9]-[01][0-9]-[0-3][0-9] [0-2][0-9]:[0-6][0-9] UTC', data_min)
  assert re.fullmatch(r'20[0-9][0-9]-[01][0-9]-[0-3][0-9] [0-2][0-9]:[0-6][0-9] UTC', data_max)
  assert origem != destino
  
  prefixo = [].copy()
  rots = descobre_todos_rec(origem, data_min, prefixo, destino, data_max, soh_disponiveis)
  return rots

def obtem_identificadores_de_trechos(rot):
  ids = [].copy()
  for trc in rot:
    assert trc != None
    sys.stderr.write("trc = %s\n" % str(trc))
    assert type(trc) is trecho.Objeto_Trecho
    ids.append(trecho.obtem_identificador(trc))
  return ids

def obtem_resumo(rot):
  resumo = {}.copy()

  trecho_inicial = rot[0]
  trecho_final = rot[-1]

  resumo['origem'] = trecho.obtem_atributo(trecho_inicial, 'origem')
  resumo['dia_partida'] = trecho.obtem_atributo(trecho_inicial, 'dia_partida')
  resumo['hora_partida'] = trecho.obtem_atributo(trecho_inicial, 'hora_partida')
  resumo['destino'] = trecho.obtem_atributo(trecho_final, 'destino')
  resumo['dia_chegada'] = trecho.obtem_atributo(trecho_final, 'dia_chegada')
  resumo['hora_chegada'] = trecho.obtem_atributo(trecho_final, 'hora_chegada')
  resumo['num_escalas'] = len(rot) - 1
  resumo['preco_min'] = 0.00 # !!! CALCULAR !!!

  return resumo

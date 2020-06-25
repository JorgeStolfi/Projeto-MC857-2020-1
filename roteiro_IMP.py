import trecho
from utils_testes import erro_prog
import sys

def descobre_todos(origem, destino, dia_min, dia_max):
  if origem == destino:
    erro_prog("origem e destino devem ser diferentes")
  # !!! Fajuto para testes !!!
  trc_VCP_SDU = trecho.busca_por_identificador("T-00000001")
  trc_SDU_POA = trecho.busca_por_identificador("T-00000004")
  rot1 = [ trc_VCP_SDU, trc_SDU_POA ]
  roteiros = [ rot1 ]
  return roteiros
 
def obtem_identificadores_de_trechos(rot):
  ids = [].copy()
  for trc in rot:
    sys.stderr.write("trc = %s\n" % str(trc))
    assert type(trc) is trecho.Objeto_Trecho
    ids.append(trecho.obtem_identificador(trc))
  return ids

def obtem_resumo(rot):

  resumo = {}

  trecho_inicial = rot[0]
  trecho_final = rot[-1]

  resumo['origem'] = trecho.obtem_atributo(trecho_inicial, 'origem')
  resumo['dia_partida'] = trecho.obtem_atributo(trecho_inicial, 'dia_partida')
  resumo['hora_partida'] = trecho.obtem_atributo(trecho_inicial, 'hora_partida')
  resumo['destino'] = trecho.obtem_atributo(trecho_final, 'destino')
  resumo['dia_chegada'] = trecho.obtem_atributo(trecho_final, 'dia_chegada')
  resumo['hora_chegada'] = trecho.obtem_atributo(trecho_final, 'hora_chegada')
  resumo['num_escalas'] = len(rot) - 1
  resumo['preco_min'] = 0.00

  return resumo
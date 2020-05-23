import trecho
from utils_testes import erro_prog

def descobre_todos(origem, destino, dia_min, dia_max):
  if origem == destino:
    erro_prog("origem e destino devem ser diferentes")
  # !!! Fajuto para testes !!!
  trc_VCP_SDU = trecho.busca_por_identificador("T-00000001")
  trc_SDU_POA = trecho.busca_por_identificador("T-00000004")
  rot1 = [ trc_VCP_SDU, trc_SDU_POA ]
  roteiros = [ rot1 ]
  return roteiros
 
def obtem_resumo(rot):
  # !!! Fajuto para testes !!!
  resumo = { 
    'origem': "VCP", 'dia_partida': "2020-05-08", 'hora_partida': "12:45",
    'destino': "MAO", 'dia_chegada': "2020-05-09", 'hora_chegada': "12:40",
    'num_escalas': 57,
    'preco_min': 2130.35
  }
  return resumo

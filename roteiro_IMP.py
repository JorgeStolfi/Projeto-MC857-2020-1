import trecho
from utils_testes import erro_prog

def descobre_todos(origem, destino, dia_min, dia_max):
  if origem == destino:
    erro_prog("origem e destino devem ser diferentes")
  # !!! Fajuto para testes !!!
  trc_VCP_SDU_1 = trecho.busca_por_identificador("T-00000001")
  trc_VCP_SDU_2 = trecho.busca_por_identificador("T-00000002")
  trc_SDU_POA_1 = trecho.busca_por_identificador("T-00000004")
  trc_POA_MAO_1 = trecho.busca_por_identificador("T-00000005")
  trc_SDU_MAO_1 = trecho.busca_por_identificador("T-00000006")
  rot1 = [ trc_VCP_SDU_1, trc_SDU_POA_1, trc_POA_MAO_1]
  rot2 = [ trc_VCP_SDU_1, trc_SDU_MAO_1 ]
  rot3 = [ trc_VCP_SDU_2, trc_SDU_MAO_1 ]
  roteiros = [ rot1, rot2, rot3 ]
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

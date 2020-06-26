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

  #  # Buscar todos os trechos com origem = {origem} com dia_partida >= {dia_min}
  #  trc_ids = trecho.busca_por_dias(dia_min, dia_max) # Selecionando os ids de trechos entre {dia_min} e {dia_max}
  #  trc_objs = [trecho.busca_por_identificador(trc) for trc in trc_ids] # Transforma os trechos em objetos
  #  # Para cada trecho a, explorar trechos b com b.origem = a.destino e b.dia_partida >= a.dia_chegada
  #  # Fazer isso até encontrar um trecho com destino = {destino} e dia_chegada <= dia_max ou não encontrar mais trechos
  #  roteiros2 = descobre_todos_rec(trc_objs, origem, destino) # faz isso recursivamente
  return roteiros

# def descobre_todos_rec(trc_objs, origem, destino):
#   trc_origem = [trc for trc in trc_objs if trc['origem'] == origem] # Seleciona apenas os trechos com origem que queremos
#   roteiros = [].copy()
#   if not trc_origem:
#     return None
#   for trc in trc_origem:
#     if trc['destino'] == destino:
#       return [trc['destino']] #retorna uma lista em que o trecho é o único elemento
#     trc_novo = [trc2 for trc2 in trc_objs if trc2['dia_partida'] > trc['dia_chegada'] or (trc2['dia_partida'] == trc['dia_chegada'] and trc2['hora_partida'] >= trc['hora_chegada'])] # trechos trc2 que partem após a chegada do trecho trc
#     roteiro = descobre_todos_rec(trc_novo, trc['origem'], destino)
#     if roteiro:
#         # Se retornou um roteiro válido, adicionar a lista à lista de roteiros desse caminho
#         pass #não implementado
#   return roteiros

def obtem_identificadores_de_trechos(rot):
  ids = [].copy()
  for trc in rot:
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
  resumo['preco_min'] = 0.00

  return resumo

import trecho
from utils_testes import erro_prog
import sys

def descobre_todos_rec(origem, destino, dia_min, dia_max, rotas, rota):
  '''Função auxiliar da função {descobre_todos}, calcula recursivamente todas os
  roteiros cujo o destino seja atingivel pela origem no intervalo de tempo
  exigido.

  Recebe {origem} e {destino} contento o ORG dos aeroportos de origem e destino,
  respectivamente;
  Recebe {dia_min} e {dia_max} especificando o intervalo de tempo que deseja-se
  partir da origem e chegar no destino;
  Recebe {rotas} que é uma lista de todos os roteiros;
  Recebe {rota} que é uma lista que contem a rota que atualmente esta sendo
  montada.

  Devolve a lista {rotas} preenchida com todos os roteiros da origem até o
  destino.'''
  for id_trecho in trecho.busca_por_origem(origem):
    trc = trecho.busca_por_identificador(id_trecho)

    attrs = trecho.obtem_atributos(trc)

    ori = attrs['origem']
    d_part = attrs['dia_partida']
    h_part = attrs['hora_partida']
    d_cheg = attrs['dia_chegada']
    h_cheg = attrs['hora_chegada']
    dest = attrs['destino']

    partida = "{} {}".format(d_part, h_part)
    chegada = "{} {}".format(d_cheg, h_cheg)

    # Verifica se o trecho parte antes do trecho esperado,
    # procure outro trecho
    if partida < dia_min:
      continue

    rota.append(trc)

    # Verifica se o trecho chega no destino na/antes da data esperada
    # Caso contrario, adiciona uma escala recursivamente
    if dest == destino and chegada <= dia_max:
      rotas.append(rota.copy())
    else:
      descobre_todos_rec(dest, destino, chegada, dia_max, rotas, rota)

    rota.pop()

def descobre_todos(origem, destino, dia_min, dia_max):
  if origem == destino:
    erro_prog("origem e destino devem ser diferentes")
  rotas = [].copy()
  rota = [].copy()
  descobre_todos_rec(origem, destino, dia_min, dia_max, rotas, rota)
  return rotas

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
  resumo['preco_min'] = 0.00

  return resumo

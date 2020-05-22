import roteiro_IMP

# Um roteiro é uma lista de um ou mais trechos que podem ser usados em seqüência
# para formar uma viagem.  No mínimo, o destino de cada trecho deve ser a origem do trecho
# seguinte, e a data + hora de chegada de cada trecho deve ser menor ou igual
# à data + hora de partida do trecho sequinte.  Além disso, cada trecho deve ter
# pelo menos uma poltrona livre.

# Mais condições podem ser acrescentadas mais tarde; por exemplo, um
# tempo mínimo em certas escalaspara mudança de veículo, alfândega, controle de
# passaportes, etc..

def descobre_todos(origem, destino, dia_min, dia_max):
  """Encontra possíveis roteiros começando no aeroporto de código {origem}
  a partir da data {dia_min}, e terminando no aeroporto de código {destino}
  até a data {dia_max}.

  Os aeroportos devem ser distintos. As datas devem estar no formato ISO
  ("YYYY-MM-DD") e referentes ao fuso hurário UTC.

  A resposta é uma lista, possivelmente vazia, de roteiros que
  satisfazem as condições dadas."""
  return roteiro_IMP.descobre_todos(origem, destino, dia_min, dia_max)

def obtem_resumo(rot):
  """Dado um roteiro {rot}, devolve um dicionário Python {atrs}
  com os dados resumidos do roteiro:

    'origem', 'dia_partida', 'hora_partida': obtidos do primeiro trecho.
    'destino', 'dia_chegada', 'hora_chegada':  obtidos do último trecho.
    'num_escalas': número de trechos menos 1 (inteiro).
    'preco_min': soma dos precos das poltronas livres mais baratos, um em cada trecho.

  Mais atributos podem ser acrescentados mais tarde.

  O roteiro {rot} deve ter pelo menos um trecho."""
  return roteiro_IMP.obtem_resumo(rot)

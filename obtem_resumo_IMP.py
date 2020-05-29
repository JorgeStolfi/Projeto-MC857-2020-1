# obtem_resumo.py

# supor que exite uma função que diz trecho_preço minimo
def obtem_resumo(rot):
  resumo = { 
    'origem': rot.origem, 'dia_partida': rot.dia_partida, 'hora_partida': rot.hora_partida,
    'destino': rot.destino, 'dia_chegada': rot.dia_chegada, 'hora_chegada': rot.hora_chegada,
    'num_escalas': rot.num_escalas,
    'preco_min': rot.preco_min
  }
  return resumo


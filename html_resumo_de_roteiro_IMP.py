from roteiro import obtem_resumo
import html_label

def gera(rot):
  # Obtem resumo
  resumo = obtem_resumo(rot)

  # Preparar Conteudo do Fragmento
  conteudo = "{} ({} {}) -- {} escalas --> {} ({} {}) valor mínimo: {}".format(resumo["origem"],       resumo["dia_partida"], \
                                                                               resumo["hora_partida"], resumo["num_escalas"], \
                                                                               resumo["destino"],      resumo["dia_chegada"], \
                                                                               resumo["hora_chegada"], resumo["preco_min"])
  ht = html_label.gera("Resumo: ", conteudo)

  return ht

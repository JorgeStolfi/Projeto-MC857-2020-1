import roteiro
import html_botao_simples

def gera(rot, ver):
  # Obtem resumo do roteiro (dicionário):
  resumo = roteiro.obtem_resumo(rot)

  # Formata campos:
  # Porto, dia, e hora de partida do primeiro trecho:
  ht_origem = resumo['origem'] 
  ht_dt_partida = resumo['dia_partida'] + " " + resumo['hora_partida'] + " UTC"
  # Porto, dia, e hora de chegada do último trecho:
  ht_destino = resumo['destino']
  ht_dt_chegada = resumo['dia_chegada'] + " " + resumo['hora_chegada'] + " UTC"
  
  ht_num_escalas = "%2d" % resumo['num_escalas']
  ht_preco_min = "%7.2f" % resumo['preco_min']
  
  campos = [ ht_origem, ht_dt_partida, ht_destino, ht_dt_chegada, ht_num_escalas, ht_preco_min  ]
  
  if ver:
    ids_trechos = roteiro.obtem_identificadores_de_trechos(rot)
    ids_trechos_txt = ",".join(ids_trechos)
    ht_ver = html_botao_simples.gera("Ver", "ver_roteiro", {'ids_trechos': ids_trechos_txt}, "#22ff22")
    campos.append(ht_ver)

  return campos

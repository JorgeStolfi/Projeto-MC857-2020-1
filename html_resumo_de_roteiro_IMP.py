import roteiro
import html_botao_simples

def gera(rot, ver):
  # Obtem resumo do roteiro (dicionário):
  resumo = roteiro.obtem_resumo(rot)

  # Formata campos:
  # Porto, dia, e hora de partida do primeiro trecho:
  ht_origem = resumo["origem"] 
  ht_dt_partida = resumo["dia_partida"] + " " + resumo["hora_partida"]
  # Porto, dia, e hora de chegada do último trecho:
  ht_destino = resumo["destino"]
  ht_dt_chegada = resumo["dia_chegada"] + " " + resumo["hora_chegada"]
  
  ht_num_escalas = resumo["num_escalas"]
  ht_preco_min = resumo["preco_min"]
  
  campos = ( ht_origem, ht_dt_partida, ht_destino, ht_dt_chegada, ht_num_escalas, ht_preco_min  )
  
  if ver:
    ids_trechos = ",".join(rot)
    ht_ver = html_botao_simples.gera("Ver", "ver_roteiro", {'ids_trechos': ids_trechos}, "#22ff22")
    campos.append(ht_ver)

  return campos

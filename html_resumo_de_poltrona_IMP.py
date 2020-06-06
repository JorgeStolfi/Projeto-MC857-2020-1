import trecho
import poltrona
import html_texto
import html_botao_submit

def gera(pol, ver, excluir):

  # lendo poltrona
  atrs_poltrona = poltrona.obtem_atributos(pol)
  id_trecho = atrs_poltrona['id_trecho']
  id_compra = atrs_poltrona['id_compra']
  preco = atrs_poltrona['preco']
  numero = atrs_poltrona['numero']

  # lendo trecho da poltrona
  trec = trecho.busca_por_identificador(id_trecho)
  atrs_trecho = trecho.obtem_atributos(trec)
  origem = atrs_trecho['origem']
  destino = atrs_trecho['destino']
  partida = atrs_trecho['dia_partida'] + ' ' + atrs_trecho['hora_partida']
  chegada = atrs_trecho['dia_chegada'] + ' ' + atrs_trecho['hora_chegada']

  ht_numero = html_texto.gera(numero, None, None, None, None, None, None, None, None)
  ht_preco = html_texto.gera(preco, None, None, None, None, None, None, None, None)
  ht_origem = html_texto.gera(origem, None, None, None, None, None, None, None, None)
  ht_destino = html_texto.gera(destino, None, None, None, None, None, None, None, None)
  ht_partida = html_texto.gera(partida, None, None, None, None, None, None, None, None)
  ht_chegada = html_texto.gera(chegada, None, None, None, None, None, None, None, None)

  linha = [ht_numero, ht_preco, ht_origem, ht_destino, ht_partida, ht_chegada] # Campos da linha, para {html_table}

  if excluir:
    ht_excluir = html_botao_submit.gera("Excluir", "excluir_poltrona", None, '#bca360')
    linha.append(ht_excluir)

  if ver:
    ht_ver = html_botao_submit.gera("Ver", 'ver_poltrona', None, '#60a3bc')
    linha.append(ht_ver)

  return linha

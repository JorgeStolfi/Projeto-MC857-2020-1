import trecho
import poltrona
import html_texto
import html_botao_submit
import html_botao_simples

def gera(pol, id_compra, ver, excluir, trocar):
  
  # Atributos da poltrona:
  id_pol = poltrona.obtem_identificador(pol)
  atrs_pol = poltrona.obtem_atributos(pol)
  assert atrs_pol['id_compra'] == id_compra

  preco_pol = atrs_pol['preco']
  numero_pol = atrs_pol['numero']

  # Atributos do trecho da poltrona
  id_trecho = atrs_pol['id_trecho']
  trc = trecho.busca_por_identificador(id_trecho)
  atrs_trc = trecho.obtem_atributos(trc)
  origem_trc = atrs_trc['origem']
  dt_partida_trc = atrs_trc['dia_partida'] + ' ' + atrs_trc['hora_partida']
  destino_trc = atrs_trc['destino']
  dt_chegada_trc = atrs_trc['dia_chegada'] + ' ' + atrs_trc['hora_chegada']

  # Campos da linha para {html_table.gera}:
  ht_trecho = html_texto.gera(id_trecho, None, None, None, None, None, None, None, None)
  ht_origem = html_texto.gera(origem_trc, None, None, None, None, None, None, None, None)
  ht_dt_partida = html_texto.gera(dt_partida_trc, None, None, None, None, None, None, None, None)
  ht_destino = html_texto.gera(destino_trc, None, None, None, None, None, None, None, None)
  ht_dt_chegada = html_texto.gera(dt_chegada_trc, None, None, None, None, None, None, None, None)

  ht_numero = html_texto.gera(numero_pol, None, None, None, None, None, None, None, None)
  ht_preco = html_texto.gera(preco_pol, None, None, None, None, None, None, None, None)

  linha = [ \
    ht_trecho, ht_origem, ht_dt_partida, ht_destino, ht_dt_chegada, 
    ht_numero, ht_preco
  ]

  ver = True # Por enquanto.
  if ver:
    args_ver = { 'id_poltrona': id_pol }
    ht_ver = html_botao_submit.gera("Ver", 'ver_poltrona', args_ver, '#60a3bc')
    linha.append(ht_ver)

  if excluir:
    args_excluir = { 'id_poltrona': id_pol, 'id_compra': id_compra }
    ht_excluir = html_botao_simples.gera("Excluir", 'excluir_poltrona', args_excluir, '#ff4422')
    linha.append(ht_excluir)

  if trocar:
    args_trocar = { 'id_poltrona': id_pol, 'id_compra': id_compra }
    ht_trocar = html_botao_submit.gera("Trocar", 'trocar_poltrona', args_trocar, '#ff8800')
    linha.append(ht_trocar)

  return linha

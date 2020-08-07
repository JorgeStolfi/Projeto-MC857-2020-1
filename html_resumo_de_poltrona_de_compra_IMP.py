import trecho
import poltrona
import html_span
import html_botao_submit
import html_botao_simples

def gera(pol, id_compra, ver, excluir):

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
  ht_trecho = html_span.gera(None, id_trecho)
  ht_origem = html_span.gera(None, origem_trc)
  ht_dt_partida = html_span.gera(None, dt_partida_trc)
  ht_destino = html_span.gera(None, destino_trc)
  ht_dt_chegada = html_span.gera(None, dt_chegada_trc)

  ht_numero = html_span.gera(None, numero_pol)
  ht_preco = html_span.gera(None, preco_pol)

  linha = [ \
    ht_trecho, ht_origem, ht_dt_partida, ht_destino, ht_dt_chegada,
    ht_numero, ht_preco
  ]
  ver = True # Por enquanto.
  if ver:
    args_ver = {'id_poltrona': id_pol}
    ht_ver = html_botao_simples.gera("Ver", 'ver_poltrona', args_ver, '#60a3bc')
    linha.append(ht_ver)
    linha.append("</form>")

  if excluir:
    args_excluir = { 'id_poltrona': id_pol, 'id_compra': id_compra }
    ht_excluir = html_botao_simples.gera("Excluir", 'excluir_poltrona', args_excluir, '#ff4422')
    linha.append(ht_excluir)

  return linha

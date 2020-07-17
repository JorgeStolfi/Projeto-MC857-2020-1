import trecho
import poltrona
import html_span
import html_botao_submit
import html_botao_simples
import sys

def gera(pol, id_trc, alterar_pol, comprar_pol, trocar_pol, id_cpr):

  assert id_trc != None
  trc = trecho.busca_por_identificador(id_trc)

  id_pol = poltrona.obtem_identificador(pol)
  atrs_pol = poltrona.obtem_atributos(pol)
  if atrs_pol['id_trecho'] != id_trc:
    sys.stderr.write("atrs_pol = %s\n" % str(atrs_pol))
  assert atrs_pol['id_trecho'] == id_trc

  preco_pol = atrs_pol['preco']
  numero_pol = atrs_pol['numero']

  # Pedido de compra à qual a poltrona pertence, ou "LIVRE":
  id_cpr_pol = atrs_pol['id_compra']
  tx_compra_pol = (id_cpr_pol if id_cpr_pol != None else "LIVRE")

  oferta_pol = atrs_pol['oferta']
  tx_oferta_pol = ("OFERTA" if oferta_pol else "")

  ht_numero = html_span.gera(None, numero_pol)
  ht_preco = html_span.gera(None, preco_pol)
  ht_oferta = html_span.gera(None, tx_oferta_pol)
  ht_compra = html_span.gera(None, tx_compra_pol)

  linha = [ht_numero, ht_preco, ht_oferta, ht_compra ]

  if alterar_pol:
    args_alterar = { 'id_poltrona': id_pol }
    ht_alterar = html_botao_simples.gera("Alterar", "solicitar_pag_alterar_poltrona", args_alterar, '#bca360')
    linha.append(ht_alterar)

  if trecho.obtem_atributo(trc, 'aberto'):
    if comprar_pol and id_cpr_pol == None:
      args_comprar = { 'id_poltrona': id_pol, 'id_compra': id_cpr }
      ht_comprar = html_botao_simples.gera("Comprar", 'comprar_poltrona', args_comprar, '#ff0000')
      linha.append(ht_comprar)

    if trocar_pol and id_cpr_pol == id_cpr:
      args_trocar = { 'id_poltrona': id_pol }
      ht_comprar = html_botao_simples.gera("Trocar", 'trocar_poltrona', args_trocar, '#ff0000')
      linha.append(ht_comprar)

  return linha

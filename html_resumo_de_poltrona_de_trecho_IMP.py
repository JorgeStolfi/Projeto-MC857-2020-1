import compra
import trecho
import poltrona
import html_span
import html_botao_submit
import html_botao_simples
import sys

def gera(pol, id_trc, admin, comprar_pol, trocar_pol, ver_oferta_pol, id_cpr):
  alterar_pol = admin
  ver_fez_checkin = admn
  realizar_checkin = admin

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
  oferta_pol = atrs_pol['oferta']
  tx_compra_pol = (id_cpr_pol if id_cpr_pol != None and oferta_pol == False else "LIVRE")

#139511 24-07-2020
  #obtendo o objeto da poltrona pelo identificador da poltrona
  id_compra = poltrona.busca_por_identificador(id_pol)
  atrs_clt = poltrona.obtem_atributos(id_compra)
  id_compra = atrs_clt["id_compra"]

  checagem = alterar_pol and (id_compra != None)
  if checagem:
    # obtendo o objeto do comprador pelo id do comprador
    atrs_cliente = compra.busca_por_identificador(id_compra)
    id_cliente = compra.obtem_atributos(atrs_cliente)
    nome_cliente = id_cliente["nome_pass"]
    doc_cliente = id_cliente["doc_pass"]
    ht_nome = html_span.gera(None, nome_cliente)
    ht_doc = html_span.gera(None, doc_cliente)
#/139511 24-07-2020

  checkin_pol = atrs_pol['fez_checkin']
  tx_checkin_pol = ("REALIZADO" if checkin_pol else "LIVRE")

  ht_numero = html_span.gera(None, numero_pol)
  ht_preco = html_span.gera(None, preco_pol)
  ht_compra = html_span.gera(None, tx_compra_pol)
  ht_fez_checkin = html_span.gera(None, tx_checkin_pol)
  ht_fazer_checkin = html_botao_simples.gera("Checkin", "fazer_checkin",None, "55ee55")

  if checagem:
    ht_numero = ht_numero + " " + ht_nome + " " + ht_doc

  linha = [ht_numero, ht_preco, ht_oferta, ht_compra, ht_fez_checkin, ht_fazer_checkin ]

  if ver_oferta_pol:
    linha.append(ht_compra)

  if trecho.obtem_atributo(trc, 'aberto'):
    if comprar_pol and id_cpr_pol == None:
      args_comprar = { 'id_poltrona': id_pol, 'id_compra': id_cpr }
      ht_comprar = html_botao_simples.gera("Comprar", 'comprar_poltrona', args_comprar, '#ff0000')
      linha.append(ht_comprar)

    if trocar_pol and id_cpr_pol == id_cpr:
      args_trocar = { 'id_poltrona': id_pol }
      ht_comprar = html_botao_simples.gera("Trocar", 'trocar_poltrona', args_trocar, '#ff0000')
      linha.append(ht_comprar)

  if alterar_pol:
    args_alterar = { 'id_poltrona': id_pol }
    ht_alterar = html_botao_simples.gera("Alterar", "solicitar_pag_alterar_poltrona", args_alterar, '#bca360')
    linha.append(ht_alterar)

  if ver_fez_checkin:
    linha.append(ht_fez_checkin)

  if realizar_checkin:
    args_checkin = { 'id_poltrona': id_pol }
    ht_checkin = html_botao_simples.gera("Checkin", "solicitar_fazer_checkin", args_checkin, "55ee55")
    linha.append(ht_checkin)

  return linha

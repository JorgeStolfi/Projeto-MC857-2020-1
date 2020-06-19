import trecho
import poltrona
import html_texto
import html_botao_submit
import sys

def gera(pol, id_trecho, alterar, comprar, id_compra):
  
  id_pol = poltrona.obtem_identificador(pol)
  atrs_pol = poltrona.obtem_atributos(pol)
  if atrs_pol['id_trecho'] != id_trecho:
    sys.stderr.write("atrs_pol = %s\n" % str(atrs_pol))
  assert atrs_pol['id_trecho'] == id_trecho
  
  preco_pol = atrs_pol['preco']
  numero_pol = atrs_pol['numero']
  
  # Pedido de compra à qual a poltrona pertence, ou "LIVRE":
  id_compra_pol = atrs_pol['id_compra']
  tx_compra_pol = (id_compra_pol if id_compra_pol != None else "LIVRE")
  
  oferta_pol = atrs_pol['oferta']
  tx_oferta_pol = ("OFERTA" if oferta_pol else "")

  ht_numero = html_texto.gera(numero_pol, None, None, None, None, None, None, None, None)
  ht_preco = html_texto.gera(preco_pol, None, None, None, None, None, None, None, None)
  ht_oferta = html_texto.gera(tx_oferta_pol, None, None, None, None, None, None, None, None)
  ht_compra = html_texto.gera(tx_compra_pol, None, None, None, None, None, None, None, None)

  linha = [ht_numero, ht_preco, ht_oferta, ht_compra ]

  ver = True # Por enquanto.
  if ver:
    args_ver = { 'id_poltrona': id_pol }
    ht_ver = html_botao_submit.gera("Ver", 'ver_poltrona', args_ver, '#60a3bc')
    linha.append(ht_ver)

  if alterar:
    args_alterar = { 'id_poltrona': id_pol }
    ht_alterar = html_botao_submit.gera("Alterar", "solicitar_pag_alterar_poltrona", args_alterar, '#bca360')
    linha.append(ht_alterar)

  if comprar and id_compra_pol == None:
    args_comprar = { 'id_poltrona': id_pol, 'id_compra': id_compra }
    ht_comprar = html_botao_submit.gera("Comprar", 'comprar_poltrona', args_comprar, '#ff0000')
    linha.append(ht_comprar)
    
  return linha

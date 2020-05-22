import compra
import html_pag_mensagem_de_erro
import html_resumo_de_compra

def gera(ses, cpr):
  id_cpr = compra.obtem_identificador(cpr)
  id_usr = compra.obtem_cliente(cpr)
  atrs_compra = compra.obtem_atributos(cpr)
  
  # Cabeçalho da compra:
  ht_resumo = html_resumo_de_compra.gera(cpr)
  
  # Lista de itens da compra
  ids_poltronas = compra.obtem_poltronas(cpr)
  detalhe_poltrona = True
  ht_itens = html_lista_de_poltronas(ses, cpr, ids_poltronas, detalhe_poltrona)
  
  ht_conteudo = ht_resumo + "<br/>" + ht_poltronas
  
  pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag

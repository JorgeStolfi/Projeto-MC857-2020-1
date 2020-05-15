import compra
import html_pag_mensagem_de_erro
import html_bloco_resumo_de_compra

def gera(ses, cpr):
  id_cpr = compra.obtem_identificador(cpr)
  id_usr = compra.obtem_cliente(cpr)
  atrs_compra = compra.obtem_atributos(cpr)
  
  # Cabeçalho da compra:
  ht_resumo = html_bloco_resumo_de_compra.gera(cpr)
  
  # Lista de itens da compra
  ids_assentos = compra.obtem_assentos(cpr)
  detalhe_assento = True
  ht_itens = html_bloco_lista_de_assentos(ses, cpr, ids_assentos, detalhe_assento)
  
  ht_conteudo = ht_resumo + "<br/>" + ht_assentos
  
  pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag

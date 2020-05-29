import compra
import html_pag_mensagem_de_erro
import html_resumo_de_compra
import html_lista_de_poltronas
import html_pag_generica

def gera(ses, cpr, excluir):
  id_cpr = compra.obtem_identificador(cpr)
  id_usr = compra.obtem_cliente(cpr)
  atrs_compra = compra.obtem_atributos(cpr)
  
  # Cabeçalho da compra:
  ver_cpr = False # Já estamos vendo a compra.
  campos_resumo = html_resumo_de_compra.gera(cpr, ver_cpr)
  
  # Lista de itens da compra
  ids_pols = compra.obtem_poltronas(cpr)
  excluir_pol = excluir
  ht_itens = html_lista_de_poltronas.gera(ses, cpr, None, ids_pols, excluir_pol)
  
  # Itera sobre os elementos vindo de "campos_resumo" transformando-os em string e concatanando para exibição da página
  ht_conteudo = ''.join(map(str, campos_resumo)) + "<br/>" + ht_itens
  
  pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag

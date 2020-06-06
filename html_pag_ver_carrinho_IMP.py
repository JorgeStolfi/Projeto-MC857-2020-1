import compra
import html_resumo_de_compra
import html_lista_de_poltronas
import html_pag_generica
import html_botao_simples


def gera(ses, cpr, erros):
  # Cabeçalho da compra:
  ver_cpr = False  # Já estamos vendo a compra.
  campos_resumo = html_resumo_de_compra.gera(cpr, ver_cpr)  # Gera lista de campos.
  campos_resumo = " ".join(campos_resumo)

  # Lista de itens da compra
  ids_pols = compra.obtem_poltronas(cpr)
  excluir_pol = True
  ht_itens = html_lista_de_poltronas.gera(ids_pols, cpr, None, excluir_pol)  # Gera "<table>...</table>"

  ht_bt_finalizar_compra = html_botao_simples.gera("Finalizar Compra", 'finalizar_compra', None, '#55ee55')

  ht_conteudo = \
    campos_resumo + "<br/>\n" + \
    ht_itens + "<br/>\n" + \
    ht_bt_finalizar_compra

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag

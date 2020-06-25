import html_lista_de_trechos
import html_pag_generica
import html_cabecalho


def gera(ses, trcs, erros):
  ht_cabe = html_cabecalho.gera("Ofertas", False)
  ht_trechos = html_lista_de_trechos.gera(trcs, alterar=False)

  ht_conteudo = \
    ht_cabe + "<br/>\n" + \
    ht_trechos

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag

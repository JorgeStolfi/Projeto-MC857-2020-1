import html_lista_de_trechos
import html_pag_generica

def gera(ses, trcs, alterar):
  ht_trechos = html_lista_de_trechos.gera(ses, trcs, alterar)
  pag = html_pag_generica.gera(ses, ht_trechos, None)
  return pag

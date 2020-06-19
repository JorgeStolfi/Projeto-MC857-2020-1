import html_lista_de_trechos
import html_pag_generica

def gera(ses, trcs, erros):
  # !!! Deveria geerar cabeçalho da página !!!
  ht_trechos = html_lista_de_trechos.gera(trcs, alterar = False)
  pag = html_pag_generica.gera(ses, ht_trechos, erros)
  return pag

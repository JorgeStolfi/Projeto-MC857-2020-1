import html_sessao
import html_pag_generica

def gera(ses, ses1, erros):
  ht_bloco_ses = html_sessao.gera(ses1)
  pag = html_pag_generica.gera(ses, ht_bloco_ses, erros)
  return pag

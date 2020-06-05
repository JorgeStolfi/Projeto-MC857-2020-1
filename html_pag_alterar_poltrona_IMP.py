import html_form_dados_de_poltrona
import html_pag_generica

def gera(ses, id_poltrona, atrs, erros):
  alterar = True
  comprar = False
  excluir = False
  id_cpr = None
  ht_form = html_form_dados_de_poltrona.gera \
    ( id_poltrona, atrs, 
      alterar = True, comprar = False, excluir = False, id_cpr = None
    )
  pag = html_pag_generica(ses, ht_form, erros)
  return pag

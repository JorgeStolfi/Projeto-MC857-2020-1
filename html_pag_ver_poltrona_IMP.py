import html_pag_generica
import html_form_dados_de_poltrona

import poltrona

def gera(ses, pol, id_compra, excluir, erros):
  alterar_pol = False
  comprar_pol = False
  excluir_pol = excluir
  ht_pol = html_form_dados_de_poltrona.gera(poltrona.obtem_identificador(pol), poltrona.obtem_atributos(pol), alterar_pol, comprar_pol, excluir_pol, id_compra)  
  ht_conteudo = ht_pol
  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag

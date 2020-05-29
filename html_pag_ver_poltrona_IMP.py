import html_poltrona
import html_pag_generica
import html_tabela

def gera(ses, pol, ver, excluir):
  polt = html_poltrona.gera(ses, pol, ver, excluir)  
  ht_conteudo = html_tabela.gera({polt})
  pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag

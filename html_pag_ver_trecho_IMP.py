import html_pag_generica
import html_texto
import html_paragrafo
import html_tabela
import html_lista_de_poltronas
import html_resumo_de_trecho

from trecho import obtem_atributos, obtem_poltronas

def gera(ses, trc):
  ver_trc = True
  alterar_trc = True
  linha_resumo = html_resumo_de_trecho.gera(trc)
  ht_resumo = " ".join(linha_resumo) 
  pols = poltrona.busca_por_trecho(trc)
  excluir_pol = False
  ht_pols = html_lista_de_poltronas.gera(ses, None, trc, pols, excluir_pol)
  ht_conteudo = ht_resumo + "<br/>" + ht_pols
  return html_pag_generica.gera(ses, ht_conteudo, None)

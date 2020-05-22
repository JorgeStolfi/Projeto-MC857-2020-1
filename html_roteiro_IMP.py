import roteiro
import html_resumo_de_roteiro
import html_lista_de_trechos

def gera(ses, rot, detalhe):
  #resumo = roteiro.obtem_resumo(rot)
  ht_resumo = html_resumo_de_roteiro.gera(rot)
  ht_trechos = ""
  
  """
  Miguel RA 174847 - 22/05/2020: Linha comentada pois a chamada da funcao html_lista_de_trechos.gera() estava com problemas.

  if detalhe:
    ht_trechos = "<br/>" + html_lista_de_trechos.gera(ses, rot, detalhe)
  """
    
  ht_tudo = ht_resumo + ht_trechos
  return ht_tudo

import roteiro
import html_resumo_de_roteiro
import html_lista_de_trechos

def gera(ses, rot, detalhe):
  resumo = roteiro.obtem_resumo(rot)
  ht_resumo = html_resumo_de_roteiro(ses, resumo)
  if detalhe:
    ht_trechos = "<br/>" + html_lista_de_trechos(ses, rot)
  else:
    ht_trechos = ""
  ht_tudo = ht_resumo + ht_trechos
  return ht_tudo

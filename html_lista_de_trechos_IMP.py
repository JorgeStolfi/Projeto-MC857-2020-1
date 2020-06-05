import trecho
import poltrona
import html_resumo_de_trecho
import html_table

def gera(trcs, alterar):
  linhas = [].copy()
  for trc in trcs:
    ver = True
    linha = html_resumo_de_trecho.gera(trc, ver, alterar)
    linhas.append(linha)
  ht_itens = html_table.gera(linhas)
  # !!! Deveria envolver tudo com um <span style="..."></span> !!!
  return ht_itens

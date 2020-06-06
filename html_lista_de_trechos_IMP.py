import trecho
import poltrona
import html_resumo_de_trecho
import html_table

def gera(trcs, alterar, excluir):
  linhas = [].copy()
  for trc in trcs:
    ver = True
    excluir_trc = excluir
    linha = html_resumo_de_trecho.gera(trc, ver, alterar, excluir_trc)
    linhas.append(linha)
  ht_itens = html_table.gera(linhas)
  ht_header = "<h1>Lista de trechos disponíveis</h1>"
  # !!! Deveria envolver tudo com um <span style="..."></span> !!!
  return ht_itens

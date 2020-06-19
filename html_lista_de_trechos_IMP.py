import trecho
import poltrona
import html_resumo_de_trecho
import html_table

def gera(trcs, alterar):
  linhas = [].copy()
  # !!! Deveria acrescentar uma linha de cabeçalho da tabela. !!!
  for trc in trcs:
    ver = True
    alterar_trc = alterar
    linha = html_resumo_de_trecho.gera(trc, ver, alterar)
    linhas.append(linha)
  ht_itens = html_table.gera(linhas)
  ht_header = "<h1>Lista de trechos disponíveis</h1>"
  # !!! Deveria envolver tudo com um <span style="..."></span> !!!
  return ht_itens

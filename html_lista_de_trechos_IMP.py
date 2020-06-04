import trecho
import poltrona
import html_resumo_de_trecho
import html_tabela

def gera(ses, trcs, alterar):
  linhas = [].copy()
  for trc in trcs:
    ver = True
    linha = html_resumo_de_trecho.gera(trc, ver, alterar)
    linhas.append(linha)
  ht_itens = html_tabela.gera(linhas)
  # !!! Deveria envolver tudo com um <span style="..."></span> !!!
  return ht_itens

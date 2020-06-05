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

  ht_header = "<h1>Lista de trechos disponíveis</h1>"

  return ht_header + ht_itens

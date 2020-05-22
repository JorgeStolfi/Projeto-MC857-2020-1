
import trecho
import html_trecho
import html_tabela

def gera(ses, trcs):
  linhas = [].copy()
  for trc in trcs:
    detalhe = False
    linha = html_trecho.gera(ses, trc, False)
    linhas.append(linha)
  # tabela
  ht_itens = html_tabela.gera(linhas)
  return ht_itens

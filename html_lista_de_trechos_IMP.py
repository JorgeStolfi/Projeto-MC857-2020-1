import trecho
import poltrona
import html_resumo_de_trecho
import html_table

def gera(trcs, alterar):
  linhas = [].copy()
  for trc in trcs:
    ver = True
    alterar_trc = alterar
    linha = html_resumo_de_trecho.gera(trc, ver, alterar)
    linhas.append(linha)
  cabecalho = ["", "Código", "Origem", "Destino", "Data de Partida", "Data de Chegada", "Número de Poltronas"]
  ht_itens = html_table.gera(linhas, cabecalho)
  # !!! Deveria envolver tudo com um <span style="..."></span> !!!
  return ht_itens

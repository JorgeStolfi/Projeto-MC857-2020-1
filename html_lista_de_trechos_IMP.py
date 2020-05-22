import html_lista_de_poltronas
import html_tabela
import html_trecho
import poltrona

def gera(ses, trcs, detalhe):
  linhas = [].copy()
  for trc in trcs:
    linha = html_trecho.gera(ses, trc, False)
    linhas.append(linha)
    if detalhe:
      pols = poltrona.busca_por_trecho(trc)
      ht_poltronas = html_lista_de_poltronas.gera(ses, pols)
      linhas.append(("", "", "", ht_poltronas))
  # tabela
  ht_itens = html_tabela.gera(linhas)
  return ht_itens

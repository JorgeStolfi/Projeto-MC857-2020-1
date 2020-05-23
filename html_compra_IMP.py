import compra
import html_tabela
import html_resumo_de_compra

def gera(cpr, detalhe):
  # Devolve o resumo da compra
  ht = html_resumo_de_compra.gera(cpr)
  if detalhe:
    # lista poltronas
    linhas = compra.obtem_itens(cpr)
    ht =  ht + html_tabela.gera(linhas)
  return ht

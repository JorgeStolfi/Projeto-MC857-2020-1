import compra
import html_table
import html_resumo_de_compra
import sys

def gera(ids_compras, ver):
  linhas = [].copy()
  # Para cada id de compra retornado
  for id_cpr in ids_compras:
    # Obtem o objeto correspondente
    compra_obj = compra.busca_por_identificador(id_cpr)

    # Gera uma lista de fragmentos HTML com as informacoes dessa compra
    campos_resumo = html_resumo_de_compra.gera(compra_obj, ver)
    # sys.stderr.write("campos_resumo = %s\n" % str(campos_resumo))
    assert type(campos_resumo) is list or type(campos_resumo) is tuple

    # Adiciona essa lista à lista de linhas para a tabela HTML:
    linhas.append(campos_resumo)
    # sys.stderr.write("linhas = %s\n" % str(linhas))

  # Gera a tabela HTML a partir da lista de linhas
  ht_itens = html_table.gera(linhas)

  # Devolve a tabela HTML
  return ht_itens

import compra
import html_cabecalho
import html_table
import html_resumo_de_compra
import html_div
import sys
import html_estilo_cabecalho_de_tabela

def gera(ids_compras, ver, id_carrinho):
  linhas = [].copy()

  # Linha de cabeçalho:
  estilo_cab = "font-size:20px;font-weight:bold; background-color: #60a3bc; color: white; padding:0px 10px 0px 0px"

  # Linha de cabeçalho:
  cabs_raw = ['CR', 'Compra', 'Usuário', 'NP', 'Passageiro', 'Documento', 'Preço' ]
  cabs_div = [].copy()
  for cb in cabs_raw:
    cabs_div.append(html_div.gera(html_estilo_cabecalho_de_tabela.gera(), cb))

  # Linhas das compras:
  for id_cpr in ids_compras:
    # Obtem o objeto correspondente
    compra_obj = compra.busca_por_identificador(id_cpr)

    # Gera uma lista de fragmentos HTML com as informacoes dessa compra
    res_campos = html_resumo_de_compra.gera(compra_obj, ver, id_carrinho)
    # sys.stderr.write("res_campos = %s\n" % str(res_campos))
    assert type(res_campos) is list or type(res_campos) is tuple

    # Adiciona essa lista à lista de linhas para a tabela HTML:
    linhas.append(res_campos)
    # sys.stderr.write("linhas = %s\n" % str(linhas))

  ht_cabe = html_cabecalho.gera("Minhas compras", False)
  # Gera a tabela HTML a partir da lista de linhas
  ht_itens = html_table.gera(linhas, cabs_div)

  ht_legenda = "CR: Seu Carrinho, NP: Número da Poltrona"

  ht_conteudo = \
        ht_cabe + "<br/>\n" + \
        ht_itens + "<br/>\n" + \
        ht_legenda

  # Devolve a tabela HTML
  return ht_conteudo

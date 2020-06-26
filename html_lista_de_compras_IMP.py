import compra
import html_table
import html_resumo_de_compra
import html_div
import sys

def gera(ids_compras, ver):
  linhas = [].copy()

  # Linha de cabeçalho:
  estilo_cab = "font-size:20px;font-weight:bold; background-color: #60a3bc; color: white; padding:0px 10px 0px 0px"
  cabs_raw = [ 'Compra', 'Usuário', 'NP', 'Passageiro', 'Documento', 'Preço' ]
  cabs_div = [].copy()
  for cb in cabs_raw:
    cabs_div.append(html_div.gera(estilo_cab, cb))
  
  linhas.append(cabs_div)

  # Linhas das compras:
  for id_cpr in ids_compras:
    # Obtem o objeto correspondente
    compra_obj = compra.busca_por_identificador(id_cpr)

    # Gera uma lista de fragmentos HTML com as informacoes dessa compra
    res_campos = html_resumo_de_compra.gera(compra_obj, ver)
    sys.stderr.write("res_campos = %s\n" % str(res_campos))
    assert type(res_campos) is list or type(res_campos) is tuple

    # Adiciona essa lista à lista de linhas para a tabela HTML:
    linhas.append(res_campos)
    # sys.stderr.write("linhas = %s\n" % str(linhas))

  # Gera a tabela HTML a partir da lista de linhas
  ht_itens = html_table.gera(linhas)

  # Devolve a tabela HTML
  return ht_itens

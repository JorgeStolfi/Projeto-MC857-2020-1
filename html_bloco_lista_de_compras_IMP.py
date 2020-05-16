import compra
import html_tabela
import html_bloco_resumo_de_compra

def gera(ses, args):
  linhas = [].copy()

  # Pega lista de compras do usuario
  compras_ids = compra.busca_por_cliente(id_usr)

  # Para cada id de compra retornado
  for id_compra in compras_ids:

      # Obtem o objeto correspondente
      compra_obj = compra.busca_por_identificador(id_compra)

      # Gera o bloco HTML com as informacoes dessa compra
      ht_resumo = html_bloco_resumo_de_compra.gera(compra_obj)

      # Adiciona o bloco HTML a lista de linhas da tabela que sera exibida
      linhas.append(( [ht_resumo] ))

  # Gera a tabela HTML a partir da lista de linhas
  ht_itens = html_tabela.gera(linhas)

  # Devolve a tabela HTML
  return ht_itens

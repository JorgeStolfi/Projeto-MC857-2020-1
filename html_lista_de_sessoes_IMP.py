import sessao
import html_resumo_de_sessao
import html_table
import html_div
import html_span
import sys
import html_estilo_cabecalho_de_tabela
import html_cabecalho

def gera(ids_sessoes, bt_ver, bt_fechar):

  # Linha de cabeçalho:
  cabs_raw = ['Sessão', 'Usuário', 'Aberta?', 'Cookie', 'Carrinho', 'Data de Criação']
  cabs_div = [].copy()
  for cb in cabs_raw:
    cabs_div.append(html_div.gera(html_estilo_cabecalho_de_tabela.gera(), cb))

  linhas = [].copy()
  for id_ses in ids_sessoes:
    # busca por id da sessao no banco
    ses = sessao.busca_por_identificador(id_ses)

    # Gera uma lista de fragmentos HTML com as informacoes dessa compra
    res_campos = html_resumo_de_sessao.gera(ses, bt_ver, bt_fechar)

    # Adiciona essa lista à lista de linhas para a tabela HTML:
    linhas.append(res_campos)
  # Gera a tabela HTML a partir da lista de linhas
  ht_itens = html_table.gera(linhas, cabs_div)

  ht_cabe = html_cabecalho.gera("Minhas Sessões", False)
  ht_conteudo = \
      ht_cabe + "<br/>\n" + \
      ht_itens

  # Devolve a tabela HTML
  return ht_conteudo

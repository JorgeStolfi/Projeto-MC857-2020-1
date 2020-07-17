import sessao
import html_resumo_de_sessao
import html_table
import html_texto
import html_div
import html_span
import sys

def gera(ids_sessoes):
  # Linha de cabeçalho:
  estilo_cab = "font-size:20px;font-weight:bold; background-color: #60a3bc; color: white; padding:0px 10px 0px 0px"
  estilo_item = "font-size:15px; background-color: #60a3bc; color: white; padding:0px 10px 0px 0px"
  cabs_raw = ['Sessão', 'Usuário', 'Aberta?', 'Cookie', 'Carrinho']
  cabs_div = [].copy()
  for cb in cabs_raw:
    cabs_div.append(html_div.gera(estilo_cab, cb))

  ## !!! (2020-07-10) Estou presumindo que o modulo html_resumo_de_sessao esta criado !!!!

  # Linhas das sessoes:
  linhas = [].copy()
  for id in ids_sessoes:
    # busca por id da sessao no banco
    ses = sessao.busca_por_identificador(id)
    assert ses != None

    # busca informacoes da sessao e passa bts
    bt_ver_ses = True
    bt_fechar_ses = False
    resumo_sessao = html_resumo_de_sessao.gera(ses, bt_ver_ses, bt_fechar_ses)
    linhas.append(resumo_sessao)

  # Gera a tabela HTML a partir da lista de linhas
  ht_itens = html_table.gera(linhas, cabs_div)

  # Devolve a tabela HTML
  return ht_itens

import sessao
import html_table
import html_texto
import html_div
import html_span
import sys
import html_estilo_cabecalho_de_tabela

def gera(ids_sessoes):

  # Linha de cabeçalho:
  cabs_raw = ['Sessão', 'Usuário', 'Aberta?', 'Cookie', 'Carrinho']
  cabs_div = [].copy()
  for cb in cabs_raw:
    cabs_div.append(html_div.gera(html_estilo_cabecalho_de_tabela.gera(), cb))
  
  ## !!! Falta implementar o modulo resumo_de_sessao para criar a lista de sessoes !!!

  # Linhas das sessoes:
  linhas = []
  for id in ids_sessoes:
    # busca sessao no banco
    ses = sessao.busca_por_identificador(id)
    assert ses != None
    # le seus atributos
    atributos = sessao.obtem_atributos(ses)
    usr = atributos['usr']
    abrt = atributos['abrt']
    cookie = atributos['cookie']
    carrinho = atributos['carrinho']

    # monta linha da tabela
    linha = [].copy()
    linha.append(html_texto.gera(id, None, None, None, None, None, None, None, None))
    linha.append(html_texto.gera(usr, None, None, None, None, None, None, None, None))
    linha.append(html_texto.gera(abrt, None, None, None, None, None, None, None, None))
    linha.append(html_texto.gera(cookie, None, None, None, None, None, None, None, None))
    linha.append(html_texto.gera(carrinho, None, None, None, None, None, None, None, None))

  # Gera a tabela HTML a partir da lista de linhas
  ht_itens = html_table.gera(linhas, cabs_div)

  # Devolve a tabela HTML
  return ht_itens

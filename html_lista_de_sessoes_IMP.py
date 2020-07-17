import sessao
import html_table
import html_div
import html_span
import sys
import html_estilo_cabecalho_de_tabela

def gera(ids_sessoes):

  # Linha de cabeçalho:
  cabs_raw = ['Sessão', 'Usuário', 'Aberta?', 'Cookie', 'Carrinho']
  cabs_div = [].copy()
  estilo_cab = html_estilo_cabecalho_de_tabela.gera()
  for cb in cabs_raw:
    cabs_div.append(html_div.gera(estilo_cab, cb))
    
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
    linha.append(html_span.gera(None, id))
    linha.append(html_span.gera(None, usr))
    linha.append(html_span.gera(None, abrt))
    linha.append(html_span.gera(None, cookie))
    linha.append(html_span.gera(None, carrinho))

  # Gera a tabela HTML a partir da lista de linhas
  ht_itens = html_table.gera(linhas, cabs_div)

  # Devolve a tabela HTML
  return ht_itens

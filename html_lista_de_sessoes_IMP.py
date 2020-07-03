import sessao
import html_table
import html_texto
import html_div
import sys

def gera(ids_sessoes):

  # Linha de cabeçalho:
  estilo_cab = "font-size:20px;font-weight:bold; background-color: #60a3bc; color: white; padding:0px 10px 0px 0px"
  estilo_item = "font-size:15px; background-color: #60a3bc; color: white; padding:0px 10px 0px 0px"
  cabs_raw = ['Sessão', 'Usuário', 'Aberta?', 'Cookie', 'Carrinho']
  cabecalho = []
  for cb in cabs_raw:
    cabecalho.append(html_div.gera(estilo_cab, cb))

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
      linha = []
      linha.append(html_texto.gera(id, None, None, None, None, None, None, None, None))
      linha.append(html_texto.gera(usr, None, None, None, None, None, None, None, None))
      linha.append(html_texto.gera(abrt, None, None, None, None, None, None, None, None))
      linha.append(html_texto.gera(cookie, None, None, None, None, None, None, None, None))
      linha.append(html_texto.gera(carrinho, None, None, None, None, None, None, None, None))
      linhas.append(linha)

  # Gera a tabela HTML a partir da lista de linhas
  ht_itens = html_table.gera(linhas, cabecalho)

  # Devolve a tabela HTML
  return ht_itens

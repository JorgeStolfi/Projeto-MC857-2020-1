import sessao
import html_table
import html_resumo_de_compra
import html_div
import html_span
import sys

def gera(ids_sessoes):
  linhas = [].copy()

  # Linha de cabeçalho:
  estilo_cab = "font-size:20px;font-weight:bold; background-color: #60a3bc; color: white; padding:0px 10px 0px 0px"
  estilo_item = "font-size:15px; background-color: #60a3bc; color: white; padding:0px 10px 0px 0px"
  cabs_raw = ['Sessao']
  cabs_div = [].copy()
  for cb in cabs_raw:
    cabs_div.append(html_div.gera(estilo_cab, cb))
  
  ## !!! Falta implementar o modulo resumo_de_sessao para criar a lista de sessoes !!!

  # Linhas das sessoes:
  for id in ids_sessoes:

    linhas.append(id)

  # Gera a tabela HTML a partir da lista de linhas
  ht_itens = html_table.gera(linhas, cabs_div)

  # Devolve a tabela HTML
  return ht_itens

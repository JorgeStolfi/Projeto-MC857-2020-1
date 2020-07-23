import trecho
import poltrona
import html_resumo_de_trecho
import html_table
import html_span
import html_estilo_cabecalho_de_tabela
import html_div

def gera(trcs, alterar):
  linhas = [].copy()
  cabecalho = [
    "", "Código", "Origem", "Data de Partida", "Destino",
    "Data de Chegada", "PLIV", "PTOT", "A partir de R$",
  ]
  cabs_div = [].copy()
  for cb in cabecalho:
    cabs_div.append(html_div.gera(html_estilo_cabecalho_de_tabela.gera(), cb))

  for trc in trcs:
    bt_ver_trc = True
    bt_alterar_trc = alterar
    bt_clonar_trc = alterar
    bt_fechar_trc = alterar
    linha = html_resumo_de_trecho.gera(trc, bt_ver_trc, bt_alterar_trc, bt_clonar_trc, bt_fechar_trc)
    linhas.append(linha)

  ht_itens = html_table.gera(linhas, cabecalho)


  estilo_texto = f"font-family: Courier; font-size: 14px; padding: 2px; text-align: left;"
  bold =  'font-weight: bold;'

  legendas = html_span.gera(estilo_texto+bold, 'Legenda<br>')
  legendas += html_span.gera(estilo_texto+bold, 'PTOT: ')
  legendas += html_span.gera(estilo_texto, 'Total de poltronas no trecho<br>')
  legendas += html_span.gera(estilo_texto+bold, 'PLIV: ')
  legendas += html_span.gera(estilo_texto, 'Poltronas livres<br>')

  return ht_itens + legendas

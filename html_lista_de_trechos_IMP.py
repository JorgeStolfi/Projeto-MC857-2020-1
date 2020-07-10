import trecho
import poltrona
import html_resumo_de_trecho
import html_table
import html_texto
import html_span
import html_estilo_cabecalho_de_tabela
import html_div

def gera(trcs, alterar):
  linhas = [].copy()
  for trc in trcs:
    bt_ver_trc = True
    bt_alterar_trc = alterar
    bt_clonar_trc = False
    bt_fechar_trc = False
    linha = html_resumo_de_trecho.gera(trc, bt_ver_trc, bt_alterar_trc, bt_clonar_trc, bt_fechar_trc)
    linhas.append(linha)
    
  cabecalho = ["", "Código", "Origem", "Data de Partida", "Destino", "Data de Chegada", "Número de Poltronas"]
  cabs_div = [].copy()
  for cb in cabecalho:
    cabs_div.append(html_div.gera(html_estilo_cabecalho_de_tabela.gera(), cb))
    
  ht_itens = html_table.gera(linhas, cabecalho)

  return ht_itens

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
    "Data de Chegada", "Poltronas livres", "Total de poltronas", "A partir de R$",
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

  return ht_itens

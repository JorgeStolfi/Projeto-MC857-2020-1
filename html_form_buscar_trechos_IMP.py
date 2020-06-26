
import html_input
import html_botao_submit
import html_botao_simples
import html_form_table
import html_form

def gera(atrs, admin):

  dados_linhas = (
      ( "Origem",           "text",        "origem",          "Cidade, aeroporto",    False, ),
      ( "Destino",          "text",        "destino",         "Cidade, aeroporto",    False, ),
      ( "Data de Partida",  "data",        "dia_partida",     "aaaa-mm-dd",           False, ),
      ( "Data de Chegada",  "data",        "dia_chegada",     "aaaa-mm-dd",           False, ),
      ( "Horario Partida",  "horario",     "hora_partida",    "hh:mm",                False, ),
      ( "Horario Chegada",  "horario",     "hora_chegada",    "hh:mm",                False, ),
      )

  ht_table = html_form_table.gera(dados_linhas, atrs, admin)
  ht_submit = html_botao_submit.gera("Buscar", "buscar_trechos", None, '#55ee55')
  ht_cancel = html_botao_simples.gera("Cancelar", "principal", None, '#ff2200')

  ht_conteudo = \
        ht_table + \
        ht_submit + \
        ht_cancel

  return html_form.gera(ht_conteudo)

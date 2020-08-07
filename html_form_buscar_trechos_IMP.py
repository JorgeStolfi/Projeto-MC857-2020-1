
import html_botao_submit
import html_botao_simples
import html_form_table
import html_form
import html_cabecalho

def gera(atrs, admin):

  ht_cabe = html_cabecalho.gera("Busca de trechos", False)

  # Dados para {html_form_table.gera}
  # {(rotulo,tipo,chave,dica,visivel,editavel,obrigatorio)}
  dados_linhas = (
    ( "Origem",                 "text",  "origem",       "Código do aeroporto",  True, True, False, ),
    ( "Data mínima de partida", "text",  "dia_partida",  "aaaa-mm-dd",           True, True, False, ),
    ( None,                     "text",  "hora_partida", "hh:mm",                True, True, False, ),
    ( "Destino",                "text",  "destino",      "Código do aeroporto",  True, True, False, ),
    ( "Data máxima de chegada", "text",  "dia_chegada",  "aaaa-mm-dd",           True, True, False, ),
    ( None,                     "text",  "hora_chegada", "hh:mm",                True, True, False, ),
  )

  ht_table = html_form_table.gera(dados_linhas, atrs)
  ht_submit = html_botao_submit.gera("Buscar", "buscar_trechos", None, '#55ee55')
  ht_cancel = html_botao_simples.gera("Cancelar", "principal", None, '#ff2200')

  ht_conteudo = \
    ht_cabe + "<br/>\n" + \
    ht_table + \
    ht_submit + \
    ht_cancel

  return html_form.gera(ht_conteudo)

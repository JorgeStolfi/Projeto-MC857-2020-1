import html_input
import html_botao_submit
import html_botao_simples
import html_form_table
import html_form

def gera(atrs, admin):

  dados_linhas = (
      ( "Tipo",            "text",         "tipo",            "Usuario, Compra, Trecho, Sessao, Assento", False),
      ( "Identificador",   "text",         "id",              "x-xxxxxxxx",                               False),
      )

  ht_table = html_form_table.gera(dados_linhas, atrs, admin)
  ht_submit = html_botao_submit.gera("Ver Objeto", "ver_objeto", None, '#55ee55')
  ht_cancel = html_botao_simples.gera("Cancelar", "principal", None, '#ff2200')

  ht_conteudo = \
        ht_table + \
        ht_submit + \
        ht_cancel

  return html_form.gera(ht_conteudo)

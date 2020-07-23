import html_input
import html_botao_submit
import html_botao_simples
import html_form_table
import html_form

def gera(atrs, admin):

  dados_linhas = (
      ( "Nome",           "text",        "nome",          "Nome",      False, ),
      ( "Email",          "text",        "email",         "Email",     False, ),
      ( "Telefone",       "text",        "telefone",      "Telefone",  False, ),
      ( "Assunto",        "text",        "assunto",       "Assunto",   False, ),
      ("Mensagem", "text", "mensagem",   "Digite sua mensagem aqui",   False,),
      )

  ht_table = html_form_table.gera(dados_linhas, atrs, admin)
  ht_submit = html_botao_submit.gera("Enviar", "enviar_msg_contato", None, '#55ee55')
  ht_cancel = html_botao_simples.gera("Cancelar", "principal", None, '#ff2200')

  ht_conteudo = \
        ht_table + \
        ht_submit + \
        ht_cancel

  return html_form.gera(ht_conteudo)

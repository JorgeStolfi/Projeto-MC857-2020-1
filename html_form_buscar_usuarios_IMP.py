
import html_botao_submit
import html_botao_simples
import html_form_table
import html_form

def gera(atrs, admin):

  # Dados para {html_form_table.gera}
  # {(rotulo,tipo,chave,dica,visivel,editavel,obrigatorio)}
  dados_linhas = (
    ( "Nome",       "text",   "nome",          "Fulano de tal",         True, True, False, ),
    ( "documento",  "text",   "documento",     "RG 4.444.444-4 SSP SP", True, True, False, ),
    ( "email",      "email",  "email",         "fulano@gmail.com",      True, True, False, ),
    ( "telefone",   "text",   "telefone",      "(XX) XXXX-XXXX",        True, True, False, ),
    ( "CPF",        "text",   "cpf",           "XXX.XXX.XXX-XX",        True, True, False, ),
    )

  ht_table = html_form_table.gera(dados_linhas, atrs)
  ht_submit = html_botao_submit.gera("Buscar", "buscar_usuarios", None, '#55ee55')
  ht_cancel = html_botao_simples.gera("Cancelar", "principal", None, '#ff2200')

  ht_conteudo = \
        ht_table + \
        ht_submit + \
        ht_cancel

  return html_form.gera(ht_conteudo)

import html_input
import html_botao_submit
import html_botao_simples
import html_form_tabela_de_campos 
import html_form

def gera(id_usuario, atrs, admin, texto_bt, cmd):
  if id_usuario != None:
    novo = False
    # Inclui campo 'id_usuario' no formulário:
    if admin != None:
      # Mostra o id do usuario somente se quem está alterando é administrador:
      ht_id_usuario = html_input.gera(None, "readonly", "id_usuario", id_usuario, True, None, None)
    else:
      ht_id_usuario = html_input.gera(None, "hidden", "id_usuario", id_usuario, True, None, None)
  else:
    novo = True
    ht_id_usuario = ""

  # For simplicity:
  if atrs == None: atrs = {}.copy()

  # Dados brutos para as linhas. Para cada linha, o rótulo, tipo do "<input>", nome do campo, e dica.
  dados_linhas = (
    ( "Nome",             "text",     "nome",          None,                  False, ),
    ( "E-mail",           "email",    "email",         "xxx@xxx.xxx.xx",      False, ),
    ( "CPF",              "text",     "CPF",           "xxx.xxx.xxx-xx",      False, ),
    ( "Telefone",         "text",     "telefone",      "+xx(xx)x-xxxx-xxxx",  False, ),
    ( "Documento",        "text",     "documento",     "Número, tipo, órgão", False, ),
    ( "Senha",            "password", "senha",         None,                  False, ),
    ( "Confirmar senha",  "password", "conf_senha",    None,                  False, ),
    ( "Administrador",    "checkbox", "administrador", None,                  True, ),
  )

  ht_tabela = html_form_tabela_de_campos.gera(dados_linhas, atrs, admin)

  ht_submit = html_botao_submit.gera(texto_bt, cmd, None, '#55ee55')

  ht_cancel = html_botao_simples.gera("Cancelar", 'principal', None, '#ee5555')

  ht_campos = \
    ( "    " + ht_id_usuario + "\n" if ht_id_usuario != "" else "") + \
    ( ht_tabela + "\n" ) + \
    ( "    " + ht_submit + "\n" ) + \
    ( "    " + ht_cancel + "\n" )
  return html_form.gera(ht_campos)


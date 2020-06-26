import html_input
import html_botao_submit
import html_botao_simples
import html_form_table
import html_form

def gera(id_usuario, atrs, admin, texto_bt, comando_bt):
  if id_usuario != None:
    novo = False
    # Inclui campo 'id_usuario' no formulário:
    if admin:
      # Mostra o id do usuario somente se quem está alterando é administrador:
      ht_id_usuario = html_input.gera(None, "readonly", "id_usuario", id_usuario, None, True, None, None)
    else:
      ht_id_usuario = html_input.gera(None, "hidden", "id_usuario", id_usuario, None, True, None, None)
  else:
    novo = True
    ht_id_usuario = ""

  # For simplicity:
  if atrs == None: atrs = {}.copy()

  # Dados brutos para as linhas. Para cada linha, o rótulo, tipo do "<input>", nome do campo, e dica.
  dados_linhas = \
    (
      ( "Nome",             "text",     "nome",          None,                  False, ),
      ( "E-mail",           "email",    "email",         "xxx@xxx.xxx.xx",      False, ),
      ( "CPF",              "text",     "CPF",           "xxx.xxx.xxx-xx",      False, ),
      ( "Telefone",         "text",     "telefone",      "+xx(xx)x-xxxx-xxxx",  False, ),
      ( "Documento",        "text",     "documento",     "Número, tipo, órgão", False, ),
      ( "Senha",            "password", "senha",         None,                  False, ),
      ( "Confirmar senha",  "password", "conf_senha",    None,                  False, ),
      ( "Administrador",    "checkbox", "administrador", None,                  True, ),
    )

  ht_table = html_form_table.gera(dados_linhas, atrs, admin)

  ht_submit = html_botao_submit.gera(texto_bt, comando_bt, None, '#55ee55')

  ht_cancel = html_botao_simples.gera("Cancelar", 'principal', None, '#ee5555')

  if admin:
      ht_botao_sessoes = html_botao_simples.gera("Ver sessões", "ver_sessoes", {'id': id_usuario}, '#eeee55')
      ht_botao_compras = html_botao_simples.gera("Ver compras", "ver_minhas_compras", {'id': id_usuario}, '#eeee55')
      ht_botao_poltronas = html_botao_simples.gera("Ver poltronas", "ver_poltronas", {'id': id_usuario}, '#eeee55')

  ht_campos = \
    ( "    " + ht_id_usuario + "\n" if ht_id_usuario != "" else "") + \
    ( ht_table + "\n" ) + \
    ( "    " + ht_submit + "\n" ) + \
    ( "    " + ht_cancel + "\n" ) + \
    ( ("   " + ht_botao_sessoes + "    " +  ht_botao_compras + "    " + ht_botao_poltronas ) if admin else "" )
  return html_form.gera(ht_campos)

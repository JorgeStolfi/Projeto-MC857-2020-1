import html_botao_submit
import html_botao_simples
import html_form_table
import html_form

def gera(id_usr, atrs, admin, ht_bt_submit):
  # Para simplificar:
  if atrs == None: atrs = {}.copy()

  novo = (id_usr == None)
  if novo:
    # Não deve haver 'id_usr' no formulário:
    if 'id_usuario' in atrs: 
      del atrs['id_usuario'] # Por via das dúvidas.
  else: 
    # Inclui campo 'id_usr' no formulário:
    atrs['id_usuario'] = id_usr
  
  # Limpa 'senha' e 'conf_senha':
  if 'senha' in atrs: del atrs['senha']
  if 'conf_senha' in atrs: del atrs['conf_senha']

  # Dados para {html_form_table.gera}
  # {(rotulo,tipo,chave,dica,visivel,editavel,obrigatorio)}
  cps = [].copy()
  if not novo:
    id_edit = False
    id_vis = admin
    cps.append(( "ID",              "text",     "id_usuario",    None,                 id_vis, id_edit, True, ))
  
  cps.append(( "Nome",            "text",     "nome",          None,                  True,  True,    True, ))
  ec_edit = novo # Email e CPF editáveis apenas na criação.
  cps.append(( "E-mail",          "email",    "email",         "xxx@xxx.xxx.xx",      True,  ec_edit, True, ))
  cps.append(( "CPF",             "text",     "CPF",           "xxx.xxx.xxx-xx",      True,  ec_edit, True, ))
  cps.append(( "Telefone",        "text",     "telefone",      "+xx(xx)x-xxxx-xxxx",  True,  True,    True, ))
  cps.append(( "Documento",       "text",     "documento",     "Número, tipo, órgão", True,  True,    True, ))
  cps.append(( "Milhagem",        "text",     "milhagem",      "Número não-negativo", True,  id_vis,  True, ))
  cps.append(( "Senha",           "password", "senha",         None,                  True,  True,    True, ))
  cps.append(( "Confirmar senha", "password", "conf_senha",    None,                  True,  True,    True, ))
  if admin:
    # Checkbox não pode ser obrigatório porque significa "Obrig. True".
    cps.append(( "Administrador",   "checkbox", "administrador", None,                  True,  True,  False, ))

  ht_table = html_form_table.gera(cps, atrs)

  ht_bt_cancel = html_botao_simples.gera("Cancelar", 'principal', None, '#ee5555')

  ht_campos = \
    ht_table + \
    ht_bt_submit + \
    ht_bt_cancel

  return html_form.gera(ht_campos)

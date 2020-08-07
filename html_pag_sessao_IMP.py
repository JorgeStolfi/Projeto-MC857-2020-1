import html_pag_generica
import html_pag_sessao
import html_botao_simples
import html_form_dados_de_sessao
import sessao
import usuario

def gera(ses, ses_ver, erros):

  # Validação dos parâmetros:
  assert ses != None # Paranóia (cliente deslogado não deve poder ver compra nenhuma).
  assert sessao.aberta(ses) # Paranóia.
  usr_ses = sessao.obtem_usuario(ses)
  assert usr_ses != None # Paranóia.
  admin = usuario.obtem_atributo(usr_ses, 'administrador')
  
  assert ses_ver != None # Paranóia.
  assert type(ses_ver) is sessao.Objeto_Sessao
  usr_ses_ver = sessao.obtem_usuario(ses_ver)
  assert admin or (usr_ses_ver == usr_ses) # Usuário comum só pode ver sessões suas.

  # Botões de acão:
  ht_submit = ""
  ht_bt_cancel = ""
  ht_dados_da_sessao = ""

  id_ses_ver = sessao.obtem_identificador(ses_ver)
  assert id_ses_ver != None # Paranóia.

  # Título da página:
  if ses_ver == ses:
    titulo = f"Sua sessao corrente {id_sessao}"
  elif usr_ses_ver == usr_ses:
    titulo = f"Sua sessao {id_sessao}"
  else:
    titulo = f"Sessao {id_sessao}"

  # Botoes de ação:
  # O submit por enquanto é só "Fechar":
  args_bt = { 'id_sessao': id_ses_ver }
  ht_submit += html_botao_submit.gera("Fechar", "fechar_sessao", None, "#ff0000")
  ht_bt_cancel = html_botao_simples.gera("Voltar", 'principal', None, "#ff2200")

  ht_titulo = "<h2>" + titlulo + "</h2>"

  # Completa {atrs} com atributos de {ses_ver}:
  atrs = {}
  args_ses_ver = sessao.obtem_atributos(ses_ver)
  assert atrs_ses_ver != None # Paranóia
  for ch, val in atrs_ses_ver.items():
    if not ch in atrs: atrs[ch] = val

  # Constrói formulário com dados do trecho:
  ht_dados_da_sessao = html_form_dados_de_sessao.gera(id_ses_ver, atrs, admin, ht_submit)

  ht_conteudo = \
    ht_titulo + "\n" + \
    ht_dados_da_sessao + "<br/>" + \
    ht_bt_cancel

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag

  ht_bloco_ses = html_form_dados_de_sessao.gera(ses_ver)

  # Somente gera botão caso o usuário da sessao atual seja administrador e a sessão selecionada esteja aberta
  if (sessao.eh_administrador(ses) and sessao.aberta(ses_ver)):
    args = {}
    args['id_sessao'] = sessao.obtem_identificador(ses_ver)

    # TODO: escolher cores melhores para os botões
    fecha_btn = html_botao_simples.gera('Fechar sessão', 'fechar_sessao', args, 'green')
    ht_bloco_ses += fecha_btn

  pag = html_pag_generica.gera(ses, ht_bloco_ses, erros)
  return pag

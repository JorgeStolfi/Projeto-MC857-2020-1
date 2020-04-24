import html_form_dados_de_usuario_IMP

def gera(id_usuario, atrs, admin, texto_bt, cmd):
  """Se {id_usuario} é {None}, retorna formulário de cadastrar novo usuário.
  Senão retorma o formulário para alterar os dados do usuário existente {usr}
  cujo identificador é {id_usuario} e cujos atributos atuais estão em {atrs}.

  O formulário terá um botão "submit" com texto {texto_bt} e ação POST {cmd}."""
  return html_form_dados_de_usuario_IMP.gera(id_usuario, atrs, admin, texto_bt, cmd)

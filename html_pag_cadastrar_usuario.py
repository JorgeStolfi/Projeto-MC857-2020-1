import html_pag_cadastrar_usuario_IMP

def gera(ses, atrs, erros):
  """Retorna uma página com o formulário de cadastramento de
  novo usuario.

  O formulário tem entradas adicionais se a sessão {ses} não for
  {None} e o usuário da mesma for um administrador.
  Vide detalhes em {html_form_cadastrar_usuario.gera}.

  Se {atrs} não for {None}, deve ser um dicionário
  que define os valores iniciais dos campos."""
  return html_pag_cadastrar_usuario_IMP.gera(ses, atrs, erros)

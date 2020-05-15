import html_pag_buscar_trecho_IMP

def gera(ses, atrs, erros):
  """Retorna uma página com o formulário de busca de trecho.

  O formulário tem entradas adicionais se a sessão {ses} não for
  {None} e o usuário da mesma for um administrador.
  Vide detalhes em {html_form_cadastrar_usuario.gera}.

  Se {atrs} não for {None}, deve ser um dicionário
  que define os valores iniciais dos campos."""
  return html_pag_buscar_trecho_IMP.gera(ses, atrs, erros)

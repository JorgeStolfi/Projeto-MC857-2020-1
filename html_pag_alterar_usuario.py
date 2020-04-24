import html_pag_alterar_usuario_IMP

def gera(ses, id_usuario, atrs, erros):
  """Retorna uma página com formulário para alterar os dados
  do usuário {usr} cujo identificador é {id_usuario}
  e cujos atributos correntes são {atrs}.

  O formulário é tem entradas adicionais se o usuário da sessão {ses}
  (NÃO o usuário que está sendo alterado) é  um administrador.
  Vide detalhes em {html_form_alterar_usuario.gera}."""
  return html_pag_alterar_usuario_IMP.gera(ses, id_usuario, atrs, erros)

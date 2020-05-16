import html_pag_alterar_trecho_IMP

def gera(ses, id_usuario, id_trecho, atrs, erros):
  """Retorna uma página com formulário para alterar os dados
  do trecho {trc} cujo identificador é {id_trecho}
  e cujos atributos correntes são {atrs}.

  O formulário é tem entradas adicionais se o usuário da sessão {ses}
  Vide detalhes em {html_form_alterar_trecho.gera}."""
  return html_pag_alterar_trecho_IMP.gera(ses, id_usuario, id_trecho, atrs, erros)

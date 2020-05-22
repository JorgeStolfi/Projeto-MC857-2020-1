import comando_solicitar_pag_acrescentar_trecho_IMP

def processa(ses, args):
  """Esta função é chamada quando o administrador aperta o botão "Acescentar Trecho"
  no menu.

  A função retorna uma página HTML {pag} com o formulário que permite ao administrador
  especificar os dados do novo trecho a ser inserido na tabela de trechos.

  O argumento {ses} deve ser uma sessão atualmente aberta.

  O dicionário de argumentos {args} deve ser vazio."""
  return comando_solicitar_pag_acrescentar_trecho_IMP.processa(ses, args)

import html_pag_criar_roteiro_IMP


def gera(ses):
  """
  Retorna uma página contendo o formulário de criar roteiro.

  Se {ses} é None ou o dono não é administrador, retorna página vazia com erro.
  """
  return html_pag_criar_roteiro_IMP.gera(ses)

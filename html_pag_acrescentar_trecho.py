import html_pag_acrescentar_trecho_IMP

def gera(ses, args, erros):
  """Retorna uma página com formulario que permite a um administrador
  especificar os dado de um trecho a ser acrescentado à tabela de trechos.  

  A sessão {ses} deve estar aberta e seu dono deve ser administrador.  

  O parâmetro {args} é um dicionário com valores iniciais a mostrar 
  nos campos do formulário; pode ser vazio.

  O parâmetro {erros} é uma lista de mensagens de erro a mostrar na página.
  Pode ser {None}. """
  return html_pag_acrescentar_trecho_IMP.gera(ses, args, erros)

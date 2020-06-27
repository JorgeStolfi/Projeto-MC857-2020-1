import comando_ver_sessoes_IMP

def processa(ses, args):
  """Esta função é chamada quando um usuário aperta o botão "Minhas compras"
  no menu geral. 
  
  A sessão corrente {ses} não pode ser {None} e deve estar aberta, e o dono dela 
  nâo deve ser um administrador.

  A função retorna uma página HTML {pag} contendo a lista de compras do usuário
  que é dono da sessão {ses}.

  O dicionário de argumentos {args} é irrelevantes e pode ser {None}."""
  return comando_ver_sessoes_IMP.processa(ses, args)

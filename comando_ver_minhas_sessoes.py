import comando_ver_minhas_sessoes_IMP

def processa(ses, args):
  """Esta função é chamada quando o administrador ou um usuário comum aperta o botão "Minhas sessoes"
  no menu geral. 
  
  Mostra as sessões do usuário da sessão {ses}.

  A função retorna uma página HTML com a lista de sessões."""
  return comando_ver_minhas_sessoes_IMP.processa(ses, args)

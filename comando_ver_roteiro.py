import comando_ver_roteiro_IMP

def processa(ses, args):
  """Esta função é chamada quando um usuário aperta o botão "Ver"
  numa lista de roteiros. 
  
  A sessão corrente {ses} não pode ser {None} e deve estar aberta.

  A função retorna uma página HTML {pag} contendo os dados do roteiro
  descrito por {args['ids_trechos']}.  Este valor deve ser um string
  que consiste de uma lista de identificadores de trechos separados 
  por vírculas, como "T-00000005,T-00001234,T-00000001"."""
  return comando_ver_roteiro_IMP.processa(ses, args)

import comando_ver_trecho_IMP

def processa(ses, args):
  """Esta função é chamada quando um usuário aperta o botão "Ver"
  numa lista de trechos. 
  
  A sessão corrente {ses} pode ser {None}.

  A função retorna uma página HTML {pag} contendo os dados da trecho
  cujo identificador é o valor de {args['id_trecho']}."""
  return comando_ver_trecho_IMP.processa(ses, args)

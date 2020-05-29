import comando_ver_compra_IMP

def processa(ses, args):
  """Esta função é chamada quando um usuário aperta o botão "Ver"
  numa lista de compras. 
  
  A sessão corrente {ses} não pode ser {None} e deve estar aberta.

  A função retorna uma página HTML {pag} contendo os dados da compra
  cujo identificador é o valor de {args['id_compra']}."""
  return comando_ver_compra_IMP.processa(ses, args)

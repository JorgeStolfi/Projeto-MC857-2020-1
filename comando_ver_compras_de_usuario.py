import comando_ver_compras_de_usuario_IMP

def processa(ses, args):
  """Esta função é chamada para exibir as compras de um usuário, dado um id
  
  A sessão corrente {ses} não pode ser {None} e deve estar aberta.

  A função retorna uma página HTML {pag} contendo a lista de compras do usuário
  pesquisado

  Dentro do dicionário de argumentos {args}, deve estar contido um {id}, que é
  o id do usuário pesquisado."""
  return comando_ver_compras_de_usuario_IMP.processa(ses, args)

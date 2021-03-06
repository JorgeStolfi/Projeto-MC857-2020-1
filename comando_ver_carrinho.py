import comando_ver_carrinho_IMP


def processa(ses, args):
  """
  Esta função é chamada quando um usuário aperta o botão "Meu Carrinho"
  no menu principal. 
  
  A sessão corrente {ses} não pode ser {None} e deve estar aberta.  O parâmetro {args}
  é ignorado.

  A função retorna uma página HTML {pag} contendo os dados da compra (carrinho atual da sessão {ses})
  com um botão de Finalizar Compra.
  """
  return comando_ver_carrinho_IMP.processa(ses, args)

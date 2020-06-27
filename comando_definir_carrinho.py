import comando_definir_carrinho_IMP


def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Definir Carrinho"
  ela deve pegar a compra selecionada em {args['id_compra']} e transformar
  num carrinho.

  A sessão corrente {ses} não pode ser {None} e deve estar aberta.

  A função retorna a página do carrinho atualizado."""
  return comando_definir_carrinho_IMP.processa(ses, args)

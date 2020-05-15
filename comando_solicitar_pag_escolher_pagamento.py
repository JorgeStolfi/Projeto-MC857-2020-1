import comando_solicitar_pag_escolher_pagamento_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Escolher pagamento"
  na página de checkout do carrinho.  
  
  A função retorna uma página HTML {pag} com o formulário de escolha de forma de pagamento.
  
  O argumento {ses} deve ser uma sessão atualmente aberta."""
  return comando_solicitar_pag_escolher_pagamento_IMP.processa(ses, args)


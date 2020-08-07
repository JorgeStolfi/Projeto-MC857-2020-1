import comando_solicitar_pag_escolher_pagamento_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Escolher pagamento"
  numa página de compra.
  
  A compra deve ter status 'comprando'.  O argumento {ses} deve ser uma sessão atualmente aberta,
  e  o usuário da sessão deve ser um administrador ou o mesmo usuário associado 
  ao pedido de compra.
  
  A função retorna uma página HTML {pag} com um formulário que permite
  ao usuário alterar a forma de pagamento."""
  return comando_solicitar_pag_escolher_pagamento_IMP.processa(ses, args)


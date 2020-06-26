import comando_finalizar_compra_IMP

def processa(ses, args):

  """Esta função é chamada quando o usuário aperta o botão "Finalizar"
  na paǵina "meu carrinho" ou "ver compra". Ela recebe a compra existente
  no carrinho pelo argumento.
  
  A compra deve ter o modo de pagamento já escolhido.

  O status da compra muda para 'pagando' """
  
  return comando_finalizar_compra_IMP.processa(ses, args)

import sessao
import compra
import comando_solicitar_pag_escolher_pagamento

def processa(ses, args):
  # Verificar se o usuário esta logado
  if ses == None:
    return html_pag_login.gera(ses,None)
  # Buscar a compra no Carrinho
  id_compra = args['id_compra'][0]
  compr = compra.busca_por_identificador(id_compra)
  # Muda status da compra para "pagando"
  compr.fecha_compra(compra_carrinho)
  # Mostrar a página de pagamento
  pag = comando_solicitar_pag_escolher_pagamento.processa(ses,compr)
  return pag

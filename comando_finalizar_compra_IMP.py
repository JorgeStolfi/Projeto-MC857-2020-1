import sessao
import compra
import html_pag_escolher_pagamento

def processa(ses, args):
  # Verificar se o usuário esta logado
  if ses == None:
    return html_pag_login.gera(ses,None)
  # Buscar a compra no Carrinho
  id_compra = args['id_compra']
  cpr = compra.busca_por_identificador(id_compra)
  # Muda status da compra para "pagando"
  compra.fecha(cpr)
  # Mostrar a página de pagamento
  pag = html_pag_escolher_pagamento.gera(ses, cpr, None)
  return pag

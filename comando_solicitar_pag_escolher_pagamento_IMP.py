
import compra
import html_pag_escolher_pagamento

def processa(ses, args):
  # !!! Verificar validade dos argumentos, devolver pag de erro se falhar !!!
  id_compra = args['id_compra']
  cpr= compra.busca_por_identificador(id_compra)
  pag = html_pag_escolher_pagamento.gera(ses, cpr, None)
  return pag
    

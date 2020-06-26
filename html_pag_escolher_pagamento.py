import html_pag_escolher_pagamento_IMP

def gera(ses, cpr, erros):
  """Retorna uma página com o formulário de escolher a forma de pagamento
  para a compra {cpr}.  
  
  A compra {cpr} deve estar em aberto. 
  Vide {html_form_escolher_pagamento.gera}."""
  return html_pag_escolher_pagamento_IMP.gera(ses, cpr, erros)

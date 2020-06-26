import html_form_escolher_pagamento_IMP

def gera(cpr):
  """Retorna o HTML do formulário para escolher a forma de pagamento
  da compra {cpr}. O formulário terá um item de multipla escolha para 
  a forma de pagamento, e um botão "Confirmar" que, quando clicado, emite
  o comando HTTP {alterar_pagamento}."""
  return html_form_escolher_pagamento_IMP.gera(cpr)

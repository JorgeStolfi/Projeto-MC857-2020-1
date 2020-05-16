import html_form_escolher_pagamento_IMP

def gera(titulo, post_url):
  """Retorna o HTML do formulário para escolher o pagamento
  O formulário contém campos radio button para escolher o tipo de pagamento a ser feitos

  Quando o usuário clicar no botão 'Enviar', será emitido um comando POST  post_url?metodo_pagamento={TIPO} """
  return html_form_escolher_pagamento_IMP.gera(titulo, post_url)

# Implementação do módulo {comando_solicitar_pag_escolher_pagamento}. 

import html_pag_escolher_pagamento

# Deixar comentado até existir o módulo que contenha o html do formulário
# import html_form_escolher_pagamento

def processa(ses, args):
  # Deixar comentado até existir o módulo que retorna o html do formulário
  # conteudo = html_form_escolher_pagamento.gera(..)
  conteudo = "Formas de pagamento"
  pag = html_pag_escolher_pagamento.gera(ses, conteudo, None)
  return pag
    
# Implementação do módulo {comando_solicitar_pag_contato}. 

import html_pag_contato

def processa(ses, args):
  pag = html_pag_contato.gera(ses, None)
  return pag
    

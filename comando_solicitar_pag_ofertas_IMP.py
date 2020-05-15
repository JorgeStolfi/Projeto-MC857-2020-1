# Implementação do módulo {comando_solicitar_pag_ofertas}. 

import html_pag_ofertas

def processa(ses, args):
  pag = html_pag_ofertas.gera(ses, args)
  return pag
    

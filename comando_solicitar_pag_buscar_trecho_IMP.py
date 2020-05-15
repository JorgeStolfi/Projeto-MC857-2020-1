# Implementação do módulo {comando_solicitar_pag_buscar_trecho}. 

import html_pag_buscar_trecho

def processa(ses, args):
  pag = html_pag_buscar_trecho.gera(ses, None, None)
  return pag
    

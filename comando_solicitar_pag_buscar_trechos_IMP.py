# Implementação do módulo {comando_solicitar_pag_buscar_trechos}. 

import html_pag_buscar_trechos

def processa(ses, args):
  pag = html_pag_buscar_trechos.gera(ses, {}, None)
  return pag
    

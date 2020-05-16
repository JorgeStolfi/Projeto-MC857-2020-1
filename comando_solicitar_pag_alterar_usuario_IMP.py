# Implementação do módulo {comando_solicitar_pag_alterar_usuario}. 

import html_pag_alterar_usuario

def processa(ses, args):
  pag = html_pag_alterar_usuario.gera(ses, None, None, None)
  return pag
    

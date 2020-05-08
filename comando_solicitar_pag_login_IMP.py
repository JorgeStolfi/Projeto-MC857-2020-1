# Implementação do módulo {comando_solicitar_pag_login}. 

import html_pag_entrar

def processa(ses, args):
  pag = html_pag_entrar.gera(ses, None)
  return pag
    

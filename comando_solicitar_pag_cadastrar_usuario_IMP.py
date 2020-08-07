# Implementação do módulo {comando_solicitar_pag_cadastrar_usuario}. 

import sessao
import html_pag_usuario

def processa(ses, args):
  usr_ses = None if ses == None else sessao.obtem_usuario(ses)  
  pag = html_pag_usuario.gera(ses, None, None, None)
  return pag
    

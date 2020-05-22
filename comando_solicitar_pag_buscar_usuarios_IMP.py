# Implementação do módulo {comando_solicitar_pag_buscar_usuario}.

import html_pag_buscar_usuario

def processa(ses, args):
  pag = html_pag_buscar_usuario.gera(ses)
  return pag
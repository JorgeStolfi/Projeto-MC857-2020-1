# Implementação do módulo {comando_solicitar_pag_buscar_usuarios}.

import html_pag_buscar_usuarios

def processa(ses, args):
  pag = html_pag_buscar_usuarios.gera(ses)
  return pag
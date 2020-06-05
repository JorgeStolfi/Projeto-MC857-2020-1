# Implementação do módulo {comando_solicitar_pag_ofertas}. 

import html_pag_ofertas
import poltrona
import sessao

def processa(ses, args):
  pols = poltrona.busca_ofertas()
  # alterar = sessao.eh_administrador(ses)
  pag = html_pag_ofertas.gera(ses, pols, None)
  return pag
    

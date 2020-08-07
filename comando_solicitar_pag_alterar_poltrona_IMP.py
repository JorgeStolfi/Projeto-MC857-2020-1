# Implementação do módulo {comando_solicitar_pag_alterar_poltrona}. 

import html_pag_poltrona
import sessao
import usuario
import poltrona

def processa(ses, args):
  
  admin = False if ses == None else sessao.eh_administrador(ses)
  assert admin # Paranóia (cliente comum e deslogado não deveria ter acesso a este cmd).

  # Obtem a poltrona a alterar:
  id_pol = args['id_poltrona'] if 'id_poltrona' in args else None
  assert id_pol != None # Paranóia (formulário deveria especificar).
  pol = poltrona.busca_por_identificador(id_pol)
  assert pol != None # Paranóia.

  pag = html_pag_poltrona.gera(ses, pol, None, None)
  return pag
    

# Implementação do módulo {comando_ver_poltrona}
import poltrona
import html_pag_poltrona
import html_pag_mensagem_de_erro

from valida_campo import ErroAtrib

def processa(ses, args):
  # Obtém id da poltrona a ver
  id_pol = args['id_poltrona'] if 'id_poltrona' in args else None
  assert id_pol != None # Paranóia (formulário deve incluir sempre).
  pol = poltrona.busca_por_identificador(id_pol)
  assert pol != None # Paranóia.

  pag = html_pag_poltrona.gera(ses, pol, None, None)
  return pag





# Implementação do módulo {comando_solicitar_pag_minhas_compras}.

import html_pag_generica
import html_pag_compra
import html_pag_mensagem_de_erro
import sessao
import usuario
import compra
import poltrona

def processa(ses, args):

  # Validações, por via das dúvidas:
  # Falhas são erros de programação e não do usuário.
  assert ses != None   # Deveria acontecer.
  assert sessao.aberta(ses)  # Deveria acontecer.
  
  usr = sessao.obtem_usuario(ses)
  assert usr != None # Deveria acontecer.

  # Obtém id da compra a ver
  id_cpr = args['id_compra'] if 'id_compra' in args else None
  assert id_cpr != None # Paranóia (formulário deve incluir sempre).
  del args['id_compra']
  cpr = compra.busca_por_identificador(id_cpr)
  assert cpr != None # Paranóia.

  # O dono da sessão pode examinar essa compra?
  autorizado = (compra.obtem_cliente(cpr) == usr) or sessao.eh_administrador(ses)
  assert autorizado # Paranóia (cliente não deveria ter acesso a compras de outros).

  pag = html_pag_compra.gera(ses, cpr, None, None)
  return pag

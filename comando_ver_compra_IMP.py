# Implementação do módulo {comando_solicitar_pag_minhas_compras}.

import html_lista_de_poltronas
import html_pag_generica
import html_pag_ver_compra
import html_pag_mensagem_de_erro
import html_pag_ver_compra
import sessao
import usuario
import compra
import poltrona

def processa(ses, args):

  # Validações, por via das dúvidas:
  assert ses != None   # Deveria acontecer.
  assert sessao.aberta(ses)  # Deveria acontecer.
  usr = sessao.obtem_usuario(ses)
  assert usr != None # Deveria acontecer.
  assert 'id_compra' in args # Deveria acontecer

  # Monta página:
  id_compra = args['id_compra']
  cpr = compra.busca_por_identificador(id_compra)
  if cpr == None:
    erros = ["compra \"" + id_compra + "\" não existe"]
    pag = html_pag_mensagem_de_erro(ses, erros)
  else:
    excluir = (compra.obtem_cliente(cpr) == usr) or usuario.eh_administrador(usr)
    pag = html_pag_ver_compra.gera(ses, cpr, excluir)
  return pag

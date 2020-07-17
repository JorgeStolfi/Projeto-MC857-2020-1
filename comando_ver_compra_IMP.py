# Implementação do módulo {comando_solicitar_pag_minhas_compras}.

import html_pag_generica
import html_pag_ver_compra
import html_pag_mensagem_de_erro
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
    # O dono da sessão pode mexer na compra?
    autorizado = (compra.obtem_cliente(cpr) == usr) or sessao.eh_administrador(ses)

    # A compra ainda pode ser alterada?
    aberto = compra.obtem_atributo(cpr, 'status') == "aberto"

    # Monta a lista de bilhetes (poltronas):
    excluir_pols = autorizado and aberto
    trocar_pols = autorizado and aberto
    pag = html_pag_ver_compra.gera(ses, cpr, excluir_pols, trocar_pols, None)
  return pag

# Implementação do módulo {comando_solicitar_pag_minhas_compras}.

import html_lista_de_compras
import html_pag_generica
import sessao
import usuario
import compra

def processa(ses, args):
  assert ses != None   # Deveria acontecer.
  assert sessao.aberta(ses)  # Deveria acontecer.
  usr = sessao.obtem_usuario(ses)
  assert usr != None # Deveria acontecer.
  assert not usuario.obtem_atributo(usr, 'administrador')  # Deveria acontecer.
  id_usr = usuario.obtem_identificador(usr)
  ids_compras = compra.busca_por_cliente(id_usr)
  ht_conteudo = html_lista_de_compras.gera(ses, ids_compras)
  pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag

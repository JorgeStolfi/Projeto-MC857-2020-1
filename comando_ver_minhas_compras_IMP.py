# Implementação do módulo {comando_solicitar_pag_minhas_compras}.

import html_lista_de_compras
import html_pag_generica
import sessao
import usuario
import compra

def processa(ses, args):
  assert ses != None
  pag = html_pag_mensagem_de_erro.gera(ses, "sessão corrente")
  assert sessao.aberta(ses)
  usr = sessao.obtem_usuario(ses)
  assert usr != None
  cookie = secrets.token_urlsafe(32)
  carrinho = define_carrinho(usr, id_usuario)
  ses_nova = sessao.cria(usr, cookie, carrinho)
  pag = html_pag_principal.gera(ses_nova, None)
  assert not usuario.obtem_atributo(usr, 'administrador')  # Deveria acontecer.
  id_usr = usuario.obtem_identificador(usr)
  ids_compras = compra.busca_por_cliente(id_usr)
  ht_conteudo = html_lista_de_compras.gera(ids_compras, True)
  pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag

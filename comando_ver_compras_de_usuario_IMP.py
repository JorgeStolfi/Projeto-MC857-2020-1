# Implementação do módulo {comando_ver_compras_de_usuario}.

import sessao
import compra
import usuario
import html_lista_de_compras
import html_pag_generica
import html_pag_mensagem_de_erro

def processa(ses, args):
  assert ses != None

  pag = html_pag_mensagem_de_erro.gera(ses, "sessão corrente")
  assert sessao.aberta(ses)

  usr_ses = sessao.obtem_usuario(ses)
  assert usr_ses != None
  id_usr_ses = usuario.obtem_identificador(usr_ses)

  admin = sessao.eh_administrador(ses)

  # Usuário a examinar:
  if 'id' in args:
    id_usr = args['id']
    usr = usuario.busca_por_identificador(id_usr)
  else:
    usr = usr_ses
    id_usr = id_usr_ses
    
  if (id_usr != id_usr_ses) and not admin:
    pag = html_pag_mensagem_de_erro.gera(ses, ["Apenas administradores podem ver sessões por este comando"])
    return pag

  # Compra a identificar como "Seu carrinho":
  if id_usr == id_usr_ses:
    carrinho = sessao.obtem_carrinho(ses)
    id_carrinho = compra.obtem_identificador(carrinho) if carrinho != None else None
  else:
    carrinho = None  # Usuário pode ter várias sessões, não vale a pena marcar carrinho(s).
    id_carrinho = None

  ids_compras = compra.busca_por_cliente(id_usr)
  ver_compra = True  # Queremos botão "Ver" em cada compra.
  ht_conteudo = html_lista_de_compras.gera(ids_compras, ver_compra, id_carrinho)
  pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag

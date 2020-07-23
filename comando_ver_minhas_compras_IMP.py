# Implementação do módulo {comando_solicitar_pag_minhas_compras}.

import html_lista_de_compras
import html_pag_generica
import html_pag_mensagem_de_erro
import sessao
import usuario
import compra
import secrets

def processa(ses, args):
  assert ses != None
  pag = html_pag_mensagem_de_erro.gera(ses, "sessão corrente")
  assert sessao.aberta(ses)
  usr = sessao.obtem_usuario(ses)
  assert usr != None
  id_usr = usuario.obtem_identificador(usr)
  ids_compras = compra.busca_por_cliente(id_usr)
  ver_compra = True  # Queremos botão "Ver" em cada compra.

  id_carrinho = ""
  if(sessao.eh_administrador(ses) == False):
    carrinho = sessao.obtem_carrinho(ses)
    if(carrinho != None):
      id_carrinho = compra.obtem_identificador(carrinho)
  
  ht_conteudo = html_lista_de_compras.gera(ids_compras, ver_compra, id_carrinho)
  pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag

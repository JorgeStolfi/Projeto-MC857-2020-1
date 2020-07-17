# Implementação do módulo {comando_ver_compras_de_usuario}.

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

  eh_administrador = sessao.eh_administrador(ses)

  if not eh_administrador:
    pag = html_pag_mensagem_de_erro.gera(ses, ["Apenas administradores podem ver sessões por este comando"])
    return pag

  id_usr = args['id']
  ids_compras = compra.busca_por_cliente(id_usr)
  ver_compra = True  # Queremos botão "Ver" em cada compra.
  ht_conteudo = html_lista_de_compras.gera(ids_compras, ver_compra)
  pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag

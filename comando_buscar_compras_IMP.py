# Implementação do módulo {comando_buscar_compras}.

import compra
import sessao
import usuario
import html_lista_de_compras
import html_pag_generica
import html_pag_buscar_compras
import html_pag_mensagem_de_erro

from valida_campo import ErroAtrib


def verifica_campos(dict, campos):
  """ Garante que todos os campos da busca são suportados pelo Objeto_Compra
  e pelo menos campo um campo de busca está definido com algo diferente de None."""

  for campo_busca in list(dict.keys()):
    if campo_busca not in campos:
      raise ErroAtrib("Campo \"%s\" inválido" % campo_busca)

  for campo in campos:
    if campo in dict and dict[campo] is not None:
      return
  raise ErroAtrib("Pelo menos um campo deve ser especificado")
  return

def processa(ses, args):
  if ses == None or not sessao.aberta(ses):
    return html_pag_mensagem_de_erro.gera(ses, "Sessão deveria estar aberta")

  try:
    if not sessao.eh_administrador(ses):
      # Usuário comum só pode buscar as próprias compras:
      usr = sessao.obtem_usuario(ses) # Dono da sessao.
      usr_id = usuario.obtem_identificador(usr)
      if not (args['cliente'] == None or args['cliente'] == usr_id):
        raise ErroAtrib("Você não tem acesso a essa informação")
      args['cliente'] = usr_id

    campos = ['cliente', 'status']
    verifica_campos(args, campos)

    cprs_ids = compra.busca_por_campos(args)
    cprs = map(lambda id_compra: compra.busca_por_identificador(id_compra), cprs_ids)
    ver = True if sessao.eh_administrador(ses) or args['cliente'] == sessao.obtem_usuario(ses) else False
    bloco = html_lista_de_compras.gera(cprs, ver)
    pag = html_pag_generica.gera(ses, bloco, None)
    return pag

  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página com mensagem de erro:
    pag = html_pag_buscar_compras.gera(ses, args, sessao.eh_administrador(ses), erros)
    return pag

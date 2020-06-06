# Implementação do módulo {comando_buscar_compras}.

import compra
import sessao
import html_lista_de_compras
import html_pag_generica
import html_pag_buscar_compras
import html_pag_mensagem_de_erro

from valida_campo import ErroAtrib


def verifica_campos(dict, campos):
  """
      Garante que:
       - Todos os campos da busca são suportados pelo Objeto_Compra
       - Pelo menos campo um campo de busca está definido com algo diferente de None
  """

  for campo_busca in list(dict.keys()):
    if campo_busca not in campos:
      del dict[campo_busca]

  for campo in campos:
    if campo in dict and dict[campo] is not None:
      return True

  return False

def processa(ses, args):
  if ses == None or not sessao.aberta(ses):
    return html_pag_mensagem_de_erro.gera(ses, "Sessão deveria estar aberta")

  if not sessao.eh_administrador(ses):
    args['cliente'] = sessao.obtem_usuario(ses)

  try:
    campos = ['cliente', 'status', 'itens']
    if not verifica_campos(args, campos):
      raise ErroAtrib("O cliente precisa ser especificado")

    compras = map(lambda id_compra: compra.busca_por_identificador(id_compra), compra.busca(args))
    ver = True if sessao.eh_administrador(ses) or args['cliente'] == sessao.obtem_usuario(ses) else False
    bloco = html_lista_de_compras.gera(compras, ver)
    pag = html_pag_generica.gera(ses, bloco, None)
    return pag

  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página com mensagem de erro:
    pag = html_pag_buscar_compras.gera(ses, args, sessao.eh_administrador(ses), erros)
    return pag

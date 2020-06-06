# Implementação do módulo {comando_buscar_usuario}.

import trecho
import sessao
import html_lista_de_usuarios
import html_pag_generica
import html_pag_buscar_usuarios

from valida_campo import ErroAtrib


def verifica_pelo_menos_um_campo(campos, dict):
  """
      Garante que:
       - Todos os campos da busca são suportados pelo Objeto_usuario
       - Todos os campos da busca estão definidos com algo diferente de None
       - Pelo menos um campo de busca está definido
  """

  for campo_busca in list(dict.keys()):
    if campo_busca not in campos:
        del dict[campo_busca]

  tem_campo = False
  for campo in campos:
    if campo in dict and dict[campo] is not None:
      if dict[campo] is None:
        del dict[campo]
      else:
        tem_campo = True
        break

  return tem_campo


def processa(ses, args):
  try:
    campos = ['nome', 'email']
    if not verifica_pelo_menos_um_campo(campos, args):
        raise ErroAtrib("Pelo menos um dos campos da busca precisa estar preenchido")

    usuarios = map(lambda id_trecho: trecho.busca_por_identificador(id_trecho), trecho.busca(args))
    alterar = sessao.eh_administrador(ses)
    bloco = html_lista_de_usuarios.gera(usuarios, alterar)
    pag = html_pag_generica.gera(ses, bloco, None)
    return pag

  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página com mensagem de erro:
    pag = html_pag_buscar_usuarios.gera(ses, args, erros)
    return pag

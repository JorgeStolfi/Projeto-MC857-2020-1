# Implementação do módulo {comando_solicitar_pag_alterar_usuario}. 

import html_pag_alterar_usuario
import sessao
import usuario

def processa(ses, args):

  # se o id_usuario nao existir, obter dados do usuario da sessao
  if args == {} or args['id_usuario'] == None :
    user = sessao.obtem_usuario(ses)
    id_usuario = usuario.obtem_identificador
  # se o id_usuario existir, obter dados do usuario desse id
  elif args['id_usuario'] != None:
    user = usuario.busca_por_identificador(args['id_usuario'])
    id_usuario = args['id_usuario']

  atrs = usuario.obtem_atributos(user)
  pag = html_pag_alterar_usuario.gera(ses, id_usuario, atrs, None)
  return pag
    

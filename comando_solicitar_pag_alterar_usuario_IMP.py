# Implementação do módulo {comando_solicitar_pag_alterar_usuario}. 

import html_pag_usuario
import sessao
import usuario

def processa(ses, args):
  if ses == None or not sessao.aberta(ses):
    erro_prog("sessão deveria estar aberta")
  else:
    usr_ses = sessao.obtem_usuario(ses)
    admin = usuario.obtem_atributo(usr_ses, 'administrador')
    
  if args == {} or args['id_usuario'] == None :
    # O 'id_usuario' nao foi especificado; supõe que é o dono da sessao:
    usr = usr_ses
    id_usr = usuario.obtem_identificador(usr)
  elif args['id_usuario'] != None:
    # O 'id_usuario' foi especificado; obtém dados do do dito cujo.
    id_usr = args['id_usuario']
    usr = usuario.busca_por_identificador(id_usr)
  else:
    erro_prog("usuário não identificado")

  atrs = usuario.obtem_atributos(usr)
  pag = html_pag_usuario.gera(ses, usr, atrs, None)
  return pag
    

# Implementação do módulo {comando_solicitar_pag_alterar_usuario}. 

import html_pag_alterar_trecho
import sessao
import usuario
import trecho

def processa(ses, args):
  erro = ''
  if ses == None or not sessao.aberta(ses):
    erro_prog("sessão deveria estar aberta")
  else:
    usr_ses = sessao.obtem_usuario(ses)
    admin = usuario.obtem_atributo(usr_ses, 'administrador')
    
  if args == {} or args['id_trecho'] == None :
    # O 'id_trecho' nao foi especificado:
    erro = 'Trecho não identificado'
    return erro
  elif args['id_trecho'] != None:
    # O 'id_trecho' foi especificado; obtém dados do dito cujo.
    id_trc = args['id_trecho']
    trc = trecho.busca_por_identificador(id_trc)
  else:
    erro_prog("Trecho não identificado")

  atrs = trecho.obtem_atributos(trc)
  pag = html_pag_alterar_trecho.gera(ses, id_trc, atrs, erro)
  return pag
    

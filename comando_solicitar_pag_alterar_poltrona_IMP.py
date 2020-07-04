# Implementação do módulo {comando_solicitar_pag_alterar_poltrona}. 

import html_pag_alterar_poltrona
import sessao
import usuario
import poltrona

def processa(ses, args):
  erro = ''
  if ses == None or not sessao.aberta(ses):
    erro = "sessão deveria estar aberta"
  else:
    usr_ses = sessao.obtem_usuario(ses)
    admin = usuario.obtem_atributo(usr_ses, 'administrador')
    
  if args == {} or args['id_poltrona'] == None :
    # O 'id_poltrona' nao foi especificado:
    erro = 'Poltrona não identificada'
    return erro
  elif args['id_poltrona'] != None:
    # O 'id_poltrona' foi especificado; obtém dados do dito cujo.
    id_pol = args['id_poltrona']
    pol = poltrona.busca_por_identificador(id_pol)
  else:
    erro = "Poltrona não identificada"

  atrs = poltrona.obtem_atributos(pol)
  pag = html_pag_alterar_poltrona.gera(ses, id_pol, atrs, erro)
  return pag
    

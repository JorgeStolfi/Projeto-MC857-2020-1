# Implementação do módulo {comando_solicitar_pag_buscar_trechos}. 

import html_pag_buscar_trechos
import sessao
import usuario

def processa(ses, args):
  # Quem está cadastrando é administrador?
  if ses != None:
    usr_ses = sessao.obtem_usuario(ses)
    admin = usuario.obtem_atributo(usr_ses, 'administrador')
  else:
    admin = False
  pag = html_pag_buscar_trechos.gera(ses, {}, admin, None)
  return pag
    

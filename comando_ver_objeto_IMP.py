import usuario
import compra
import sessao
import trecho
import assento

import html_pag_ver_usuario
import html_pag_ver_compra
import html_pag_ver_sessao
import html_pag_ver_trecho
import html_pag_ver_assento

import html_pag_mensagem_de_erro

def processa(ses, args):
  # !!! deveria exigir que o dono da sessao seja administrador !!!
  if 'id' in args:
    id = args['id']
    letra = id[0]
    if letra == "U":
      usr = usuario.busca_por_identificador(id)
      pag = html_pag_ver_usuario.gera(ses, usr)
    elif letra == "C":
      cpr = compra.busca_por_identificador(id)
      pag = html_pag_ver_compra.gera(ses, cpr)
    elif letra == "T":
      tre = trecho.busca_por_identificador(id)
      pag = html_pag_ver_trecho.gera(ses, tre)
    elif letra == "S":
      ses1 = sessao.busca_por_identificador(id)
      pag = html_pag_ver_sessao.gera(ses, ses1)
    elif letra == "A":
      ass = assento.busca_por_identificador(id)
      pag = html_pag_ver_assento.gera(ses, ass)
    else: 
      pag = html_pag_mensagem_de_erro.gera(ses, "Classe de objeto \"" + letra + "\" inválida")
    return pag
    

import usuario
import compra
import sessao
import trecho
import poltrona

import html_pag_ver_usuario
import html_pag_ver_compra
import html_pag_ver_sessao
import html_pag_ver_trecho
import html_pag_ver_poltrona

import html_pag_mensagem_de_erro
import sys #added by shimeji


def processa(ses, args):
  # !!! deveria exigir que o dono da sessao seja administrador !!!
  #begin changes
  privilegio_usuario = sessao.eh_administrador(ses)
  #sys.stderr.write("CHECANDO ARGS: %s lalala " % sera_q)

  #end changes
  if 'id' in args:
    id = args['id']
    letra = id[0]
    if privilegio_usuario:
      if letra == "U":
        usr = usuario.busca_por_identificador(id)
        pag = html_pag_ver_usuario.gera(ses, usr, None)
      elif letra == "C":
        cpr = compra.busca_por_identificador(id)
        pag = html_pag_ver_compra.gera(ses, cpr, False, None)
      elif letra == "T":
        trc = trecho.busca_por_identificador(id)
        pag = html_pag_ver_trecho.gera(ses, trc, False, False, None)
      elif letra == "S":
        ses1 = sessao.busca_por_identificador(id)
        pag = html_pag_ver_sessao.gera(ses, ses1, None)
      elif letra == "A":
        pol = poltrona.busca_por_identificador(id)
        pag = html_pag_ver_poltrona.gera(ses, pol, False, None)
      else: 
        pag = html_pag_mensagem_de_erro.gera(ses, "Classe de objeto \"" + letra + "\" inválida")
      return pag
    

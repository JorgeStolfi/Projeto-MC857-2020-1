import usuario
import compra
import sessao
import trecho
import poltrona
from valida_campo import ErroAtrib

import html_pag_usuario
import html_pag_compra
import html_pag_sessao
import html_pag_trecho
import html_pag_poltrona

import html_pag_mensagem_de_erro
import sys #added by shimeji


def processa(ses, args):
  usr_ses = None if ses == None else sessao.obtem_usuario(ses)
  assert sessao.eh_administrador(ses) # O dono da sessão deve ser administrador.
  try:
    if not 'id' in args:
      pag = html_pag_mensagem_de_erro.gera(ses, 'É necessário adicionar um ID para pesquisar.')
      return pag

    id = args['id']
    if len(id) != 10: raise ErroAtrib("O identificador \"" + id + "\" é inválido")
    
    letra = id[0]
    if letra == "U":
      usr = usuario.busca_por_identificador(id)
      if usr == None: raise ErroAtrib("Não existe usuário com identificador " + id)
      usr_atrs = usuario.obtem_atributos(usr)
      usr_atrs['id_usuario'] = usuario.obtem_identificador(usr)
      pag = html_pag_usuario.gera(ses, usr, usr_atrs, None)
    elif letra == "C":
      cpr = compra.busca_por_identificador(id)
      if cpr == None: raise ErroAtrib("Não existe pedido de compra com identificador" + id)
      pag = html_pag_compra.gera(ses, cpr, None, None)
    elif letra == "T":
      trc = trecho.busca_por_identificador(id)
      if trc == None: raise ErroAtrib("Não existe trecho de viagem com identificador" + id)
      pag = html_pag_trecho.gera(ses, trc, None, None)
    elif letra == "S":
      ses_a_ver = sessao.busca_por_identificador(id)
      if ses_a_ver == None: raise ErroAtrib("Não existe sessão com identificador" + id)
      pag = html_pag_sessao.gera(ses, ses_a_ver, None)
    elif letra == "A":
      pol = poltrona.busca_por_identificador(id)
      if pol == None: raise ErroAtrib("Não existe poltrona com identificador" + id)
      pag = html_pag_poltrona.gera(ses, pol, None, None)
    else:
      raise ErroAtrib("Classe de objeto \"" + letra + "\" inválida")
  except ErroAtrib as ex:
    erros = ex.args[0]
    return html_pag_mensagem_de_erro.gera(ses, erros)
  return pag


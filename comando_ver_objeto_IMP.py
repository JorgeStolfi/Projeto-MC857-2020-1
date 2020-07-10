import usuario
import compra
import sessao
import trecho
import poltrona
from valida_campo import ErroAtrib

import html_pag_ver_usuario
import html_pag_ver_compra
import html_pag_ver_sessao
import html_pag_ver_trecho
import html_pag_ver_poltrona

import html_pag_mensagem_de_erro
import sys #added by shimeji


def processa(ses, args):
  assert sessao.eh_administrador(ses) # O dono da sessão deve ser administrador.
  assert 'id' in args # O dicionário {args} deve conter campo 'id'.
  try:
    id = args['id']
    if len(id) != 10: raise ErroAtrib("O identificador \"" + id + "\" é inválido")
    letra = id[0]
    if letra == "U":
      usr = usuario.busca_por_identificador(id)
      if usr == None: raise ErroAtrib("Não existe usuário com identificador " + id)
      pag = html_pag_ver_usuario.gera(ses, usr, None)
    elif letra == "C":
      cpr = compra.busca_por_identificador(id)
      if cpr == None: raise ErroAtrib("Não existe pedido de compra com identificador" + id)
      excluir_pols = False # Pois o dono da sessão deve ser admin, que não pode comprar.
      trocar_pols = False  # Pois o dono da sessão deve ser admin, que não pode comprar.
      pag = html_pag_ver_compra.gera(ses, cpr, excluir_pols, trocar_pols, None)
    elif letra == "T":
      trc = trecho.busca_por_identificador(id)
      if trc == None: raise ErroAtrib("Não existe trecho de viagem com identificador" + id)
      comprar_pols = False  # Pois o dono da sessão deve ser admin, que não pode comprar.
      alterar_trc = True    # Pois o dono da sessão deve ser admin.                      
      id_cpr = None         # Pois o dono da sessão deve ser admin, que não tem carrinho.
      pag = html_pag_ver_trecho.gera(ses, trc, comprar_pols, alterar_trc, None)
    elif letra == "S":
      ses1 = sessao.busca_por_identificador(id)
      if ses1 == None: raise ErroAtrib("Não existe sessão com identificador" + id)
      pag = html_pag_ver_sessao.gera(ses, ses1, None)
    elif letra == "A":
      pol = poltrona.busca_por_identificador(id)
      if pol == None: raise ErroAtrib("Não existe poltrona com identificador" + id)
      excluir_pol = False  # Pois o dono da sessão deve ser admin, que não tem carrinho.
      id_cpr = None        # Pois o dono da sessão deve ser admin, que não tem carrinho.
      pag = html_pag_ver_poltrona.gera(ses, pol, id_cpr, excluir_pol, None)
    else:
      raise ErroAtrib("Classe de objeto \"" + letra + "\" inválida")
  except ErroAtrib as ex:
    erros = ex.args[0]
    return html_pag_mensagem_de_erro.gera(ses, erros)
  return pag


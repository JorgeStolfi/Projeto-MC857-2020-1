# Implementação do módulo {comando_comprar poltrona}.

import poltrona
import compra
import sessao
import usuario
import html_pag_ver_compra
import html_pag_principal
from valida_campo import ErroAtrib

def processa(ses, args):
  try:
    if ses == None:
       raise ErroAtrib("Precisa logar para comprar")
    usr_ses = sessao.obtem_usuario(ses)
    assert usr_ses != None
    if usuario.obtem_atributo(usr_ses, 'administrador'):
      raise ErroAtrib("Administrador não pode comprar")

    id_pol = args["id_pol"]
    assert id_pol is not None, "faltou argumento 'id_pol'"

    cpr = sessao.obtem_carrinho(ses)
    assert cpr != None
    id_cpr = compra.obtem_identificador(cpr)

    # Muda a poltrona para comprada
    pol = poltrona.busca_por_identificador(id_pol)
    assert pol != None
    assert poltrona.obtem_atributo(pol, 'id_compra') == None # Poltrona deve estar livre.
    poltrona.muda_atributos(pol, { 'id_compra': id_cpr })

    excluir = True # Mostra botão "Excluir" em cada poltrona.
    trocar = True # Mostra botão "Trocar" em cada poltrona.
    pag = html_pag_ver_compra.gera(ses, cpr, excluir, trocar, None)
  except ErroAtrib as ex:
    erros = ex.args[0]
    pag = html_pag_principal.gera(ses, erros)
  return pag

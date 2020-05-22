# Implementação do módulo {comando_buscar_trecho}.

import trecho
import html_lista_de_trechos
import html_pag_generica
import html_pag_buscar_trecho

from valida_campo import ErroAtrib

def processa(ses, args):
  try:
    if 'destino' not in args:
      raise ErroAtrib("campo 'destino' deve ser preenchido")
    if 'origem' not in args:
      raise ErroAtrib("campo 'origem' deve ser preenchido")
    ids_trechos = trecho.busca_por_origem_e_destino(args['destino'], args['origem'])
    bloco = html_lista_de_trechos.gera(ses, ids_trechos)
    pag = html_pag_generica.gera(ses, bloco, None)
    return pag

  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página com mens de erro:
    pag = html_pag_buscar_trecho.gera(ses, args, erros)
    return pag

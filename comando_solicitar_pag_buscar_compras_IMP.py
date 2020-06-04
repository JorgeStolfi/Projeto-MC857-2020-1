import html_pag_buscar_compras


def processa(ses, args):
  pag = html_pag_buscar_compras.gera(ses)
  return pag

# Implementação do módulo {comando_solicitar_pag_minhas_compras}.

import html_bloco_lista_de_compras
import html_pag_generica

def processa(ses, args):

  ht_conteudo = html_bloco_lista_de_compras.gera(ses, args)

  pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag

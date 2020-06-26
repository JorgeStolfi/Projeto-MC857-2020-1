# Implementação do módulo {comando_definir_carrinho}.

import trecho
import sessao
import html_lista_de_trechos
import html_pag_generica
import html_pag_buscar_trechos
import sys

from valida_campo import ErroAtrib


def processa(ses, args):
  ht_conteudo = "<label> Função </label><br/>\n"
  pag = html_pag_generica.gera(ses, ht_conteudo, None)
  return pag

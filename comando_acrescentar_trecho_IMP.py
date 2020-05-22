# Implementação do módulo {comando_acrescentar_trecho}.

import html_pag_principal
import html_pag_acrescentar_trecho
import trecho
import sessao
from utils_testes import erro_prog, mostra
from valida_campo import ErroAtrib
import re
import sys

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, atrs):
  # Tenta criar o trecho:
  try:
    trc = trecho.cria(atrs)
    pag = html_pag_principal.gera(ses, None)
  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página de acrescentar trecho com os mesmos argumentos e mens de erro:
    pag = html_pag_acrescentar_trecho.gera(ses, atrs, erros)
  return pag
  

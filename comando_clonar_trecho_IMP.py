# Implementação do módulo {comando_clonar_trecho}.

import html_pag_principal
import html_pag_alterar_trecho
import trecho
import sessao
import poltrona
from utils_testes import erro_prog, mostra
from valida_campo import ErroAtrib
import re
import sys

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, atrs):

  try:
    # Separa o atributo 'poltronas' em {val_pos}:
    if 'poltronas' in atrs:
      esp_pols = atrs['poltronas'] # String que especfica poltronas e preços.
      del atrs['poltronas']
    else:
      raise ErroAtrib("Coloque as poltronas do trecho.\"")
    # Tenta criar o trecho:

    trc = trecho.cria(atrs)
    pag = html_pag_principal.gera(ses, None)
    # pols = poltrona.cria_conjunto(trc, esp_pols)
  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página de alterar trecho com os mesmos argumentos e mens de erro:
    pag = html_pag_alterar_trecho.gera(ses,None, atrs, erros, True)
  return pag
  

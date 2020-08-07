# Implementação do módulo {comando_acrescentar_trecho}.

import html_pag_trecho
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
    assert 'encerrado' in atrs
    if atrs['encerrado'] == 'on': atrs['encerrado'] = True # Necessario?

    trc = trecho.cria(atrs)
    pols = poltrona.cria_conjunto(trc, esp_pols)

    # Mostra o trecho criado:
    pag = html_pag_trecho.gera(ses, trc, None, "Trecho criado")
  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página de acrescentar trecho com os mesmos argumentos e mens de erro:
    pag = html_pag_trecho.gera(ses, None, atrs, erros)
  return pag

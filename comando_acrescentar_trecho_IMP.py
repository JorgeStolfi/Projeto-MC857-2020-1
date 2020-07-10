# Implementação do módulo {comando_acrescentar_trecho}.

import html_pag_acrescentar_trecho
import html_pag_ver_trecho
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

    if 'aberto' not in atrs:
        atrs['aberto'] = False
    else:
        atrs['aberto'] = atrs['aberto'] == 'on' or atrs['aberto']

    trc = trecho.cria(atrs)
    pols = poltrona.cria_conjunto(trc, esp_pols)

    # Mostra o trecho criado:
    comprar_pols = False  # Pois o dono da sessão deve ser admin, que não pode comprar.
    alterar_trc = True    # Pois o dono da sessão deve ser admin.
    id_cpr = None         # Pois o dono da sessão deve ser admin, que não tem carrinho.
    pag = html_pag_ver_trecho.gera(ses, trc, comprar_pols, alterar_trc, id_cpr)
  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página de acrescentar trecho com os mesmos argumentos e mens de erro:
    pag = html_pag_acrescentar_trecho.gera(ses, atrs, erros)
  return pag

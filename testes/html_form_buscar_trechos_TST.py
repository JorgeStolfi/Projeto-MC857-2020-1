#! /usr/bin/python3
 
# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import html_form_buscar_trechos
import trecho
import identificador
import base_sql
import tabelas
import sessao
import compra
import utils_testes
import comando_alterar_usuario

import sys

# Testes das funções de {html_form}:

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_form_buscar_trechos
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Teste01: {atrs} = valores e {admin} = {True}
atr = { 
        'origem':       "OIA",
        'destino':      "MOA",
      }
admin = True

testa("Valores_Admin", atr, admin)

# Teste02: {atrs} = valores e {admin} = {False}
atr = { # T-00000001
        'origem':       "VCP",
        'destino':      "SDU",
      }
admin = False

testa("Valores_Comum", atr, admin)

# Teste03: {atrs} = valores e {admin} = {True}
atr = { 
        'origem':       "",
        'destino':      "",
      }
admin = True

testa("Sem_Valores_Admin", atr, admin)

# Teste04: {atrs} = valores e {admin} = {False}
atr = { # T-00000001
        'origem':       "",
        'destino':      "",
      }
admin = False

testa("Sem_Valores_Comum", atr, admin)


#! /usr/bin/python3

# Interfaces usadas por este script:

import html_div
import utils_testes

import sys

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{rotulo}.html"."""
  
  modulo = html_div
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa("N", "font-family: 'Courier'; font-size: 30px", "Hello World")


#! /usr/bin/python3

import html_form_tabela_de_campos
import base_sql
import identificador
import sessao
import tabelas
import usuario
import utils_testes
import sys

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = gera_html_form
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

assert False # !!! NÃO IMPLEMENTADO !!!

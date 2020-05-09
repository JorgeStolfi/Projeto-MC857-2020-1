#! /usr/bin/python3

import html_bloco_erro
import base_sql
import tabelas
import usuario
import sessao
import compra
import utils_testes

import sys

# Testes das funções de {html_bloco_erro}:

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_bloco_erro
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa("1", "Você errou, meu amigo!")
testa("2", "Você errou, meu amigo!\nE errou de novo!")
testa("L", [ "Você errou, meu amigo!", "E errou de novo!" ])
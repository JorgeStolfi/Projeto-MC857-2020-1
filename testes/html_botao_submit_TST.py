#! /usr/bin/python3

import html_botao_submit
import utils_testes
import sys

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_botao_submit
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

testa("Cadastrar",        "Cadastrar", 'cadastrar_usuario', None, '#55ee55')

testa("Alterar_usuario",  "Alterar", 'alterar_usuario', {'id_usuario': "U-00000001"}, '#55ee55')

testa("Entrar",           "Entrar", 'fazer_login', None, '#55ee55')

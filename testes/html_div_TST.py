#! /usr/bin/python3

# Interfaces usadas por este script:

import html_div
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Testes das funções de {gera_html_elem}:

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/gera_{modulo}.{rotulo}.html"."""
  
  modulo = html_div
  frag = True
  utils_testes.testa_gera_html(modulo, modulo.gera, rotulo, frag, *args)

testa("N", "font-family: 'Courier'; font-size: 30px", "Hello World")


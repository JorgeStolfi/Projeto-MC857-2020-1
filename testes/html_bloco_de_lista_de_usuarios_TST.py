#! /usr/bin/python3

# Interfaces usadas por este script:

import html_bloco_de_lista_de_usuarios
import base_sql
import tabelas
import usuario
import sessao
import compra
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

def testa(rotulo,  funcao, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/gera_{modulo}.{rotulo}.html"."""
  
  modulo = html_bloco_de_lista_de_usuarios
  frag = True
  pretty = True
  utils_testes.testa_gera_html(modulo, getattr(modulo, funcao), rotulo, frag, pretty, *args)

usr1_ident = "U-00000001"
usr2_ident = "U-00000002"
usr5_ident = "U-00000005"

testa("N", "gera", [usr1_ident,usr5_ident,usr2_ident])

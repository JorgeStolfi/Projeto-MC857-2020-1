#! /usr/bin/python3

# Interfaces usadas por este script:

import html_lista_de_usuarios
import base_sql
import tabelas
import usuario
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_lista_de_usuarios
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

usr1_ident = "U-00000001"
usr2_ident = "U-00000002"
usr3_ident = "U-00000003"

testa("N", [usr1_ident,usr3_ident,usr2_ident]) # este teste funciona pois todos usuarios sao criados
#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import html_form_login
import usuario
import identificador
import base_sql
import tabelas
import utils_testes


import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

# Testes das funções de {html_form}:

def testa(rotulo):
  """Testa {funcao()}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_form_login
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty)

usr1 = usuario.busca_por_identificador("U-00000001")
assert usr1 != None

testa("N")

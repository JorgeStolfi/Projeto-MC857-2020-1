#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import html_form_dados_de_usuario
import usuario
import identificador
import base_sql
import tabelas
import sessao
import compra
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Testes das funções de {gera_html_form}:

def testa(rotulo,  funcao, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/gera_html_form.{rotulo}.html"."""
  
  modulo = html_form_dados_de_usuario
  frag = True
  utils_testes.testa_gera_html(modulo, getattr(modulo, funcao), rotulo, frag, *args)

ses = sessao.busca_por_identificador("S-00000001")
assert ses != None
assert sessao.aberta(ses)

usr1 = sessao.obtem_usuario(ses)
assert usr1 != None

cpr1_ident = "C-00000001"
cpr1 = compra.busca_por_identificador(cpr1_ident)
assert cpr1 != None

testa("gera", "gera", usr1)

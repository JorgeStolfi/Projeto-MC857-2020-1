#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

import html_form_dados_de_sessao
import sessao
import identificador
import base_sql
import tabelas
import utils_testes

import sys

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_form_dados_de_sessao
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# fixtures
sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

# Testes das funções de {gera_html_form}:
ses1 = sessao.busca_por_identificador("S-00000001")
assert ses1 != None
testa("S", ses1)

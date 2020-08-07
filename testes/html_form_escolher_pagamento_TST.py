#! /usr/bin/python3

# Este programa pode ser usado para testar funções que
# escrevem formulários HTML5.

# Interfaces usadas por este script:
import html_form_escolher_pagamento
import compra
import tabelas
import base_sql
import utils_testes
import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes(False)

# Testes das funções de {html_form}:

def testa(rotulo, *args):
  """Testa {funcao()}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_form_escolher_pagamento
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

cpr1 = compra.busca_por_identificador("C-00000002")
assert compra.obtem_status(cpr1) == 'comprando'
testa("N", cpr1)

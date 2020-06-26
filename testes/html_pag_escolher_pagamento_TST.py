#! /usr/bin/python3

import html_pag_escolher_pagamento
import tabelas
import sessao
import compra
import base_sql
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Sessao de teste
ses = sessao.busca_por_identificador("S-00000001")

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_pag_escolher_pagamento
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

for tag, sess, id_compra, erros in (
    ("N", ses,    'C-00000001', None),
    ("N-S", None, 'C-00000002', None),
    ("V", ses,    'C-00000003', []),
    ("E", ses,    'C-00000004', ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",])
  ):
  cpr = compra.busca_por_identificador(id_compra)
  testa(tag, ses, cpr, erros)

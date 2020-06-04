#! /usr/bin/python3

import html_pag_escolher_pagamento
import tabelas
import sessao
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

for tag, sess, conteudo, erros in (
    ("N", ses, r'Teste', None),
    ("N-S", None, r'Teste', None),
    ("V", ses, r'Teste', []),
    ("E", ses, r'Teste', ["Mensagem UM", "Mensagem DOIS", "Mensagem TRÊS",])):

  testa(tag, sess, conteudo, erros)

#! /usr/bin/python3

import html_trecho
import html_tabela
import utils_testes
import base_sql
import tabelas
import trecho
import sessao

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

def testa(rotulo, ses, trc, detalhe):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_trecho
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = True # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).

  nome_fn = funcao.__name__
  func_rot = nome_fn + "." + rotulo

  res = funcao(ses, trc, detalhe)

  if detalhe:
    utils_testes.testa_modulo_html(modulo, func_rot, res, frag, pretty)
  else:
    tab = html_tabela.gera({res})
    utils_testes.testa_modulo_html(modulo, func_rot, tab, frag, pretty)

ses = sessao.busca_por_identificador("S-00000001")
trc = trecho.busca_por_identificador("T-00000001")

testa("1", ses, trc, False)
testa("2", ses, trc, True)

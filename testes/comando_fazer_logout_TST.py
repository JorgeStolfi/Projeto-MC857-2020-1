#! /usr/bin/python3

# Interfaces usadas por este script:

import comando_fazer_logout
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

# Testes das funções de {html_bloco_erro}:

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = comando_fazer_logout
  res = modulo.processa(args[0], *args)
  assert res
  sys.stdout.write(res[0])

ses = sessao.busca_por_identificador("S-00000001")
assert ses != None
assert sessao.aberta(ses)

testa("A", ses)

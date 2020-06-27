#! /usr/bin/python3

# Interfaces usadas por este script:

import comando_fechar_sessao
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

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = comando_fechar_sessao
  funcao = modulo.processa
  frag = False
  pretty = False
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

id_sessao = "S-00000003"
ses = sessao.busca_por_identificador(id_sessao)
assert ses != None
assert sessao.aberta(ses)

testa("A", ses, {'id_sessao':id_sessao})

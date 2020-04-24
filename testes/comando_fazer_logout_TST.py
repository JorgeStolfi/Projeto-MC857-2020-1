#! /usr/bin/python3

# Interfaces usadas por este script:

import base_sql
import tabelas
import usuario
import produto
import sessao
import compra
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Testes das funções de {html_bloco_de_erro}:

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/html_{modulo}.{rotulo}.html"."""

ses = sessao.busca_por_identificador("S-00000001")
assert ses != None
assert sessao.aberta(ses)

usr = sessao.obtem_usuario(ses)
assert usr != None

sessao.fecha(ses)

if ses:
    testa("N", "Você errou, meu amigo!")
else:
    testa("S", "Você acertou, meu amigo!")

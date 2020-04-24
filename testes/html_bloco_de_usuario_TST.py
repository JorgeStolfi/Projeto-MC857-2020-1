#! /usr/bin/python3

# Interfaces usadas por este script:

import html_bloco_de_usuario
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

# Testes das funções de {gera_html_elem}:

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/html_{modulo}.{rotulo}.html"."""
  
  modulo = html_bloco_de_usuario
  frag = True
  utils_testes.testa_gera_html(modulo, modulo.gera, rotulo, frag, *args)

usr1_ident = "U-00000001"
usr1 = usuario.busca_por_identificador(usr1_ident)
usr2_ident = "U-00000002"
usr5_ident = "U-00000005"

testa("N-F",  usr1_ident, usr1)
testa("N-T", usr1_ident, usr1)
testa("10-F",  usr1_ident, usr1)
testa("10-T", usr1_ident, usr1 )


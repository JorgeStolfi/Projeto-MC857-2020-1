#! /usr/bin/python3

# Interfaces usadas por este script:

import html_resumo_de_usuario
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
  
  modulo = html_resumo_de_usuario
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

usr1_ident = "U-00000001"
usr1 = usuario.busca_por_identificador(usr1_ident)
usr2_ident = "U-00000002"
usr5_ident = "U-00000005"

testa("N",  usr1)


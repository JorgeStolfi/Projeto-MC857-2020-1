#! /usr/bin/python3
# Interfaces usadas por este script:

import html_pag_ver_roteiro
import base_sql
import tabelas
import roteiro
import utils_testes
import sessao

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  
  modulo = html_pag_ver_roteiro
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

ses1 = sessao.busca_por_identificador("S-00000001")

rots = roteiro.descobre_todos("VCP", "MAO", "2020-05-07", "2020-05-10", False)
rot = rots[0]

testa("N-E0", None, rot, None) # Sem login
testa("N-E1", None, rot, "Ó mundo cruel") # Sem login

ses1 = sessao.busca_por_identificador("S-00000001")

testa("L-E0", ses1, rot, None) # Com login


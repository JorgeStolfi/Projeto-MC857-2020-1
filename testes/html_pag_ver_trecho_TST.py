#! /usr/bin/env python3

import html_pag_ver_trecho
import tabelas
import usuario
import sessao
import trecho
import base_sql
import utils_testes

import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("Criando alguns objetos...\n")
tabelas.cria_todos_os_testes()

# Sessao de teste:
ses = sessao.busca_por_identificador("S-00000001")
assert ses != None

# Usuario teste:
usr1 = sessao.obtem_usuario(ses)
assert usr1 != None
usr1_id = usuario.obtem_identificador(usr1)
usr1_atrs = usuario.obtem_atributos(usr1)

# Trecho teste
trecho1 = trecho.busca_por_identificador("T-00000001")
assert trecho1 != None

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_pag_ver_trecho
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# Testes com erros em vérios formatos:
for comprar in (False, True):
  for alterar in (False, True):
    ca = "-c" + str(comprar) + "-a" + str(alterar)
    for tag, erros in (
        ("N-E0", None), 
        ("N-E1", "Não entendi"), 
      ):
      testa(tag + ca, ses, trecho1, comprar, alterar, erros)

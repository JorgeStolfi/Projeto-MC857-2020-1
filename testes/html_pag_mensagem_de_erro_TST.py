#! /usr/bin/python3

import tabelas
import sessao
import base_sql
import utils_testes
import usuario
import compra
import html_pag_mensagem_de_erro


import sys

sys.stderr.write("Conectando com base de dados...\n")
res = base_sql.conecta("DB",None,None)
assert res == None
usuario.inicializa(False)
usuario.cria_testes()
compra.inicializa(False)
compra.cria_testes()
sessao.inicializa(False)
sessao.cria_testes()
ses = sessao.busca_por_identificador("S-00000001")
assert ses != None

def testa(rotulo, *args):
  """Testa {funcao(*args)}, grava resultado
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

  modulo = html_pag_mensagem_de_erro
  funcao = modulo.gera
  frag = False  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  utils_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

for tag, erros in (
    ("N", None),
    ("V", []),
    ("1", "Você cometeu um erro, rapaz!"),
    ("2", "Você cometeu um erro, rapaz!\nE outro erro também!"),
    ("L", ["Você cometeu um erro, rapaz!", "E outro erro também!", "E mais um!"])
  ):
  rotulo = tag
  testa(rotulo, ses, erros)
